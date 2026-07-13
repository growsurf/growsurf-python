# Changelog

## [1.2.0](https://github.com/growsurf/growsurf-python/compare/v1.1.2...v1.2.0) (2026-07-13)


### Features

* **api:** add Team resource ([9efbfbd](https://github.com/growsurf/growsurf-python/commit/9efbfbdfec10336d473f9266a033d93c3e98bb9e))

## [1.1.2](https://github.com/growsurf/growsurf-python/compare/v1.1.1...v1.1.2) (2026-07-11)


### Bug Fixes

* support retry-safe API key rotation ([8656a44](https://github.com/growsurf/growsurf-python/commit/8656a4469e8e48a6ad7252ad1c9241d8cef09ee2))

## [1.1.1](https://github.com/growsurf/growsurf-python/compare/v1.1.0...v1.1.1) (2026-07-09)


### Bug Fixes

* remove referral screenshot REST surface ([28e5902](https://github.com/growsurf/growsurf-python/commit/28e59029205433515d7797b99985fd480ed3a67a))
* skip mobile token mock tests ([b3592eb](https://github.com/growsurf/growsurf-python/commit/b3592eb63df762cb7539250f6c939f265a7a9fe1))


### Documentation

* reduce PyPI badge cache ([358dd6d](https://github.com/growsurf/growsurf-python/commit/358dd6dc1a69895e12a87772e77561e967f2cf2d))

## [1.1.0](https://github.com/growsurf/growsurf-python/compare/v1.0.0...v1.1.0) (2026-07-08)


### Features

* add account webhook and participant APIs ([6b8fc27](https://github.com/growsurf/growsurf-python/commit/6b8fc2734e28322d8d6891295e8d3a4a2487c1d5))


### Bug Fixes

* sort Python SDK imports ([e3a8a9d](https://github.com/growsurf/growsurf-python/commit/e3a8a9dc9b3793bad975c4c3951287ceeea20733))

## [1.0.0](https://github.com/growsurf/growsurf-python/compare/v0.8.0...v1.0.0) (2026-07-03)


### ⚠ BREAKING CHANGES

* campaign create no longer accepts `options`, and campaign update no longer accepts the design / emails / options / notifications / installation config blobs — edit those via the new config sub-resources. Reward-config CRUD moved from /campaign/{id}/rewards to /campaign/{id}/reward-configs[/{campaignRewardId}].

### Features

* add campaign management endpoints; drop deprecated create/update config blobs ([6116f40](https://github.com/growsurf/growsurf-python/commit/6116f400534856bfeafcafa21a42fd648b167fe5))

## [0.8.0](https://github.com/growsurf/growsurf-python/compare/v0.7.0...v0.8.0) (2026-07-01)


### Features

* **api:** add campaign create/update/clone and program-reward CRUD ([ef2fee0](https://github.com/growsurf/growsurf-python/commit/ef2fee0997638e5461988d514ab5505c63436b35))

## 0.7.0 (2026-06-29)

Full Changelog: [v0.6.1...v0.7.0](https://github.com/growsurf/growsurf-python/compare/v0.6.1...v0.7.0)

### Features

* **api:** support delayed referral rewards and affiliate refunds ([f0afb36](https://github.com/growsurf/growsurf-python/commit/f0afb361ec64165cbb21134d277e8ad224a57106))

## 0.6.1 (2026-06-26)

Full Changelog: [v0.6.0...v0.6.1](https://github.com/growsurf/growsurf-python/compare/v0.6.0...v0.6.1)

## 0.6.0 (2026-06-23)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/growsurf/growsurf-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** add payoutSettings to Participant ([f1c59b5](https://github.com/growsurf/growsurf-python/commit/f1c59b55b06e1082f725d6df2fa5057458250347))
* **api:** manual updates ([e949eb6](https://github.com/growsurf/growsurf-python/commit/e949eb62d25a5c1c67176b77199dee46abb161f8))


### Bug Fixes

* **auth:** prioritize first auth header ([c398225](https://github.com/growsurf/growsurf-python/commit/c39822597c0c851137b6a3b6ef954f8831e1601b))

## 0.5.0 (2026-05-25)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/growsurf/growsurf-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** manual updates ([6b45870](https://github.com/growsurf/growsurf-python/commit/6b458706424429c9f9b269b2968fcace87d0a3b5))

## 0.4.0 (2026-05-20)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/growsurf/growsurf-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** Add Participant.mobileInstanceId ([0dc8db9](https://github.com/growsurf/growsurf-python/commit/0dc8db9d24e075b782975aaa5236281fb8d4c5fd))

## 0.3.0 (2026-05-19)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/growsurf/growsurf-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** manual updates ([fa106aa](https://github.com/growsurf/growsurf-python/commit/fa106aacec6012c1edd197e17f39bd05fb0396ec))

## 0.2.0 (2026-05-15)

Full Changelog: [v0.1.1...v0.2.0](https://github.com/growsurf/growsurf-python/compare/v0.1.1...v0.2.0)

### Features

* **api:** manual updates ([fd54cd8](https://github.com/growsurf/growsurf-python/commit/fd54cd81f974f1db00aac592f457fe6e7b4af86a))

## 0.1.1 (2026-05-13)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/growsurf/growsurf-python/compare/v0.1.0...v0.1.1)

## 0.1.0 (2026-05-12)

Full Changelog: [v0.0.2...v0.1.0](https://github.com/growsurf/growsurf-python/compare/v0.0.2...v0.1.0)

### Features

* **api:** manual updates ([31c14cf](https://github.com/growsurf/growsurf-python/commit/31c14cfba6611cc5c974230e9e2584e6f6b3a7a3))
* **internal/types:** support eagerly validating pydantic iterators ([c6cd14c](https://github.com/growsurf/growsurf-python/commit/c6cd14c45e8a652f511ca9c31de194c4cd140d2d))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([7a3c356](https://github.com/growsurf/growsurf-python/commit/7a3c356587c6b2ea311c1f28723fd86a946db5db))


### Chores

* update SDK settings ([434e9ce](https://github.com/growsurf/growsurf-python/commit/434e9cec74d6101510ca7f45261e981b8362121f))

## 0.0.2 (2026-05-08)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/growsurf/growsurf-python/compare/v0.0.1...v0.0.2)

### Chores

* configure new SDK language ([45e223b](https://github.com/growsurf/growsurf-python/commit/45e223bb712c113de22d73b12dabd150307ff0e1))
* update SDK settings ([3368d8c](https://github.com/growsurf/growsurf-python/commit/3368d8c79567e764db5dee2420698817db835109))
* update SDK settings ([442bdaa](https://github.com/growsurf/growsurf-python/commit/442bdaafd0413d3804a0ccea1c198ec9168c8517))
* update SDK settings ([900e620](https://github.com/growsurf/growsurf-python/commit/900e620e1902fc15a2ea4a2cd9161a5044a580ed))
* update SDK settings ([b76870e](https://github.com/growsurf/growsurf-python/commit/b76870e2ecdd17bdf523eeaf2375b8373ab6fe95))
* update SDK settings ([e017f0e](https://github.com/growsurf/growsurf-python/commit/e017f0e0a8f06a3d106bcabd04692ea13ed068b1))
