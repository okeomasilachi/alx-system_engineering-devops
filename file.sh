#!/bin/bash
val=$(env)
sleep 2
echo "$val" | grep SHELL
