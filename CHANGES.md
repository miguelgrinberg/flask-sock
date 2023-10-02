# Flask-Sock change log

**Release 0.7.0** - 2023-10-02

- Avoid crashes on WebSocket exit in debug mode [#70](https://github.com/miguelgrinberg/flask-sock/issues/70) ([commit](https://github.com/miguelgrinberg/flask-sock/commit/78cf5d19e8ceccc366b029755341e822e578d003))
- Clock example [#45](https://github.com/miguelgrinberg/flask-sock/issues/45) ([commit](https://github.com/miguelgrinberg/flask-sock/commit/fde3c8e2b8795603f4a8bea202d105e8c886c31a)) (thanks **Gilbert Brault**!)
- Remove unused import in documentation example [#43](https://github.com/miguelgrinberg/flask-sock/issues/43) ([commit](https://github.com/miguelgrinberg/flask-sock/commit/568776ab2e4068065b75dea4a3051cc264a6891a)) (thanks **Ali-Akber Saifee**!)

**Release 0.6.0** - 2022-12-24

- Option to attach WebSocket route to a blueprint ([commit](https://github.com/miguelgrinberg/flask-sock/commit/3bfacdee99006a6db170d12b2988d41f4376e210))
- Example multi-file application ([commit](https://github.com/miguelgrinberg/flask-sock/commit/10e0b3bb05580b63433106ef1b5ab42a735846d6))
- Add Pyton 3.11 to build ([commit](https://github.com/miguelgrinberg/flask-sock/commit/245abe67838c6dd4feeaed35450dd32b8e39dec3))

**Release 0.5.2** - 2022-03-17

- Pass WebSocket server options in the configuration [#7](https://github.com/miguelgrinberg/flask-sock/issues/7) ([commit](https://github.com/miguelgrinberg/flask-sock/commit/126c86a133fa5d56a5539e784bd0252f8f94140a))

**Release 0.5.1** - 2022-03-11

- Prevent AssertionError with Werkzeug when connection ends ([commit](https://github.com/miguelgrinberg/flask-sock/commit/f6142a60ec666f8dd440235dffb86fe7a55c2642))

**Release 0.5.0** - 2022-02-17

- Clean close of the WebSocket connection when possible [#20](https://github.com/miguelgrinberg/flask-sock/issues/20) ([commit](https://github.com/miguelgrinberg/flask-sock/commit/32f5d060105512b98b064081f6c441885d24e323))
- Avoid duplicate variable names in examples ([commit](https://github.com/miguelgrinberg/flask-sock/commit/8f42c60f87c81437a56a43d7b91ea2d33a2d3ca0))
- Unit tests ([commit](https://github.com/miguelgrinberg/flask-sock/commit/9b2e335b2bdb566def9c206a5fffb7269d9904ad))
- API reference documentation ([commit](https://github.com/miguelgrinberg/flask-sock/commit/18b1cc080e56bfd81dc10d12e8de731c220a9dee))
- Update builds for python 3.10 and pypy3.8 ([commit](https://github.com/miguelgrinberg/flask-sock/commit/d337288ac7d7bb878cfe9609e1f6703300b51ed4))

**Release 0.4.0** - 2021-06-06

- More robustness when the connection is closed ([commit](https://github.com/miguelgrinberg/flask-sock/commit/1a323e55109aa0dc524ea46ee6742ba69263416c))
- Add a dependency on Flask 2.x ([commit](https://github.com/miguelgrinberg/flask-sock/commit/d8e15f476d151855e8a3d8715090877f5886b2dd))
- Add a change log ([commit](https://github.com/miguelgrinberg/flask-sock/commit/fab096164c9eee5142eb940f28df763ab533be5f))
- Documentation ([commit](https://github.com/miguelgrinberg/flask-sock/commit/3c8761bc8b52ff9c0b3d16d9b96c47b2260e7b85))
- More examples ([commit](https://github.com/miguelgrinberg/flask-sock/commit/66b458dc131a5bf75731aaf888b42aa0d2e4e58c))
- GitHub builds ([commit](https://github.com/miguelgrinberg/flask-sock/commit/6733afdb2aea763e43ac42d6528f474cc3bd40c4))
- Unit testing framework ([commit](https://github.com/miguelgrinberg/flask-sock/commit/e7eeb425bd72cfb266be03c7d4eaa57d72d19f7a))

**Release 0.3.0** - 2021-05-10

- Move generic WebSocket code to [simple-websocket](https://github.com/miguelgrinberg/simple-websocket) package ([commit](https://github.com/miguelgrinberg/flask-sock/commit/b3d5ecb31495430d6eda7b88830c8f4cca51e192))

**Release 0.2.0** - 2021-04-14

- Updated readme ([commit](https://github.com/miguelgrinberg/flask-sock/commit/4ffdcecfb8949327db6cdeb7a25fad1ca11507ec))
- Add support for eventlet and gevent ([commit](https://github.com/miguelgrinberg/flask-sock/commit/ac6d3077ca4f37af3b63dd1d0ab263031ae9bc49))

**Release 0.1.0** - 2021-04-03

- Handle path arguments correctly ([commit](https://github.com/miguelgrinberg/flask-sock/commit/a9a216b7892a2fd5c23118a548d647a4820bf23e))
- Added minimal usage documentation to readme file ([commit](https://github.com/miguelgrinberg/flask-sock/commit/7f8c8fd53f43dae427263b98a3268d42603187b9))

**Release 0.0.5** - 2021-03-28

- Close method ([commit](https://github.com/miguelgrinberg/flask-sock/commit/8c0895c351a4e6b9379f784f48c0e02394d5d030))

**Release 0.0.4** - 2021-03-27

- Better code organization ([commit](https://github.com/miguelgrinberg/flask-sock/commit/8a89e2999d05fa1274dcf6583fb07c0f9bf2ac47))

**Release 0.0.3** - 2021-03-27

- Remove dependency on Flask request from WebSocket class ([commit](https://github.com/miguelgrinberg/flask-sock/commit/1f856ad35ad1f330d22cf5af62c10ded21a86e75))
- Add ConnectionClosed exception ([commit](https://github.com/miguelgrinberg/flask-sock/commit/e1bcadf85ff5e142604fef18cbf6d83e5d935db1))
- Added HTML template to echo example ([commit](https://github.com/miguelgrinberg/flask-sock/commit/65ef8373e7ec0aa1019c0d1764d0d64e24c78a3a))

**Release 0.0.2** - 2021-03-27

- First commit ([commit](https://github.com/miguelgrinberg/flask-sock/commit/4161939e7c75e20903c92148f6fbd215c3178139))
