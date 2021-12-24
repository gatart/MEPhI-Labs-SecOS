#!/bin/bash

ps -eo "%u%u%c" | awk '{if ($1 != $2) print $3}'
