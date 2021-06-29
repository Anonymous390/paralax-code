from typing import Any

import pygame
from pygame import display, event, time
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT

from .helpers import (check_lost, clear_rows, convert_shape_format,
                      create_grid, draw_next_shape, draw_text_middle,
                      draw_window, get_shape, high_score, update_score,
                      valid_space)
from .objects import Shape


class Menu:
    def __init__(self, window: Any) -> None:
        pygame.init()
        self.window = window
        self.menu_running = True
        self.window_fill = (0, 0, 0)
        self.screen_msg = 'Press Any Key To Play'
        self.screen_msg_size = 60
        self.screen_msg_color = (255, 255, 255)

    def run(self) -> None:
        while self.menu_running:
            self.window.fill(self.window_fill)
            draw_text_middle(
                self.window,
                self.screen_msg,
                self.screen_msg_size,
                self.screen_msg_color,
            )
            display.update()
            for input in event.get():
                if input.type == QUIT:
                    self.menu_running = False
                if input.type == KEYDOWN:
                    Game(self.window).start()
        display.quit()


class Interface:
    def __init__(self, window) -> None:
        self.window = window
        self.game_running = True
        self.grid: Any
        self.locked_position: dict = {}
        self.clock = time.Clock()
        self.change_piece = False
        self.curr_piece = get_shape()
        self.next_piece = get_shape()
        self.high_score = high_score()
        self.curr_score = 0
        self.fall_time = 0
        self.level_time = 0
        self.level_time_max = 5
        self.fall_speed_max = 0.27
        self.time_div = 1000
        self.lvl_time_obs_float_0 = 0.12
        self.lvl_time_obs_float_1 = 0.005
        self.lost_msg = "YOU LOST"
        self.lost_msg_size = 80
        self.lost_msg_color = (255, 255, 255)

    def _clear_rows(self) -> int:
        return clear_rows(self.grid, self.locked_position) * 10

    def _get_shape(self) -> Shape:
        return get_shape()

    def _convert_shape(self) -> list:
        return convert_shape_format(self.curr_piece)

    def _check_valid_space(self) -> bool:
        return valid_space(self.curr_piece, self.grid)

    def _draw_text_mid(
        self,
        msg: str = "",
        msg_size: int = 50,
        msg_color: tuple[int, int, int] = (0, 0, 0)) -> None:
        draw_text_middle(self.window, msg, msg_size, msg_color)

    def _draw_window(self) -> None:
        draw_window(self.window, self.grid, self.curr_score, self.high_score)

    def _draw_next_shape(self) -> None:
        draw_next_shape(self.next_piece, self.window)

    def _update_score(self) -> None:
        update_score(self.curr_score)

    def _update_display(self) -> None:
        display.update()

    def _quit_display(self) -> None:
        display.quit()

    def _time_delay(self) -> None:
        time.delay(1500)


class Game(Interface):
    def start(self):
        while self.game_running:
            self.grid = create_grid(self.locked_position)
            self.fall_time += self.clock.get_rawtime()
            self.level_time += self.clock.get_rawtime()
            self.clock.tick()
            self.level()
            self.key_event()
            self.piece_change()
            self.refresh_frame()

    def level(self):
        if self.level_time > self.lvl_time_obs_float_0:
            self.level_time -= self.lvl_time_obs_float_1

        if self.level_time / self.time_div > self.level_time_max:
            self.level_time = 0

        if self.fall_time / self.time_div > self.fall_speed_max:
            self.fall_time = 0
            self.curr_piece.y += 1

        if not self._check_valid_space() and self.curr_piece.y > 0:
            self.curr_piece.y -= 1
            self.change_piece = True

    def key_event(self):
        for input in event.get():
            if input.type == QUIT:
                self.game_running = False
                self._quit_display()

            prev_piece_pos_x = self.curr_piece.x
            prev_piece_pos_y = self.curr_piece.y
            prev_piece_pos_r = self.curr_piece.rotation

            if input.type == KEYDOWN:
                if input.key == K_LEFT:
                    self.curr_piece.x -= 1
                if input.key == K_RIGHT:
                    self.curr_piece.x += 1
                if input.key == K_DOWN:
                    self.curr_piece.y += 1
                if input.key == K_UP:
                    self.curr_piece.rotation += 1

            if not self._check_valid_space():
                if self.curr_piece.x != prev_piece_pos_x:
                    self.curr_piece.x = prev_piece_pos_x
                if self.curr_piece.y != prev_piece_pos_y:
                    self.curr_piece.y = prev_piece_pos_y
                if self.curr_piece.rotation != prev_piece_pos_r:
                    self.curr_piece.rotation = prev_piece_pos_r

    def piece_change(self) -> None:
        self.shape_pos = self._convert_shape()

        for i in range(len(self.shape_pos)):
            x, y = self.shape_pos[i]
            if y > -1:
                self.grid[y][x] = self.curr_piece.color

        if self.change_piece:
            for pos in self.shape_pos:
                pos_vals = (pos[0], pos[1])
                self.locked_position[pos_vals] = self.curr_piece.color

            self.curr_piece = self.next_piece
            self.next_piece = self._get_shape()
            self.curr_score += self._clear_rows()
            self.change_piece = False

    def refresh_frame(self):
        self._draw_window()
        self._draw_next_shape()
        self._update_display()

        if check_lost(self.locked_position):
            self._draw_text_mid(self.lost_msg, self.lost_msg_size,
                                self.lost_msg_color)
            self._update_display()
            self._time_delay()
            self._update_score()
            self.game_running = False
