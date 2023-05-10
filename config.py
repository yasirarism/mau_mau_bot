#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from dotenv import load_dotenv
from os import environ

load_dotenv("config.env", override=True)

TOKEN=environ.get("TOKEN")
WORKERS=environ.get("WORKERS", 32)
ADMIN_LIST = environ.get("ADMIN_LIST", None)
OPEN_LOBBY = environ.get("OPEN_LOBBY", True)
ENABLE_TRANSLATIONS = environ.get("ENABLE_TRANSLATIONS", False)
DEFAULT_GAMEMODE = environ.get("DEFAULT_GAMEMODE", "fast")
WAITING_TIME = environ.get("WAITING_TIME", 120)
TIME_REMOVAL_AFTER_SKIP = environ.get("TIME_REMOVAL_AFTER_SKIP", 20)
MIN_FAST_TURN_TIME = environ.get("MIN_FAST_TURN_TIME", 15)
MIN_PLAYERS = environ.get("MIN_PLAYERS", 2)
