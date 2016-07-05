#!/usr/bin/env python3.4


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    yield b'Hello World!\n'
