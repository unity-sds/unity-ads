# Changelog

All notable changes for the Unity Application Development Serves will be documented in this file. This combines changes across multiple repositories.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

--------

## [Unity Release 23.1] - 2023-04-07

### Repository Tags

- [unity-ads-deployment](https://github.com/unity-sds/unity-ads-deployment/) : [0.3.0](https://github.com/unity-sds/unity-ads-deployment/releases/tag/0.3.0)
- [unity-docker-stacks](https://github.com/unity-sds/unity-docker-stacks) : [0.1.0](https://github.com/unity-sds/unity-docker-stacks/releases/tag/0.1.0)
- [app-pack-generator](https://github.com/unity-sds/app-pack-generator) : [0.1.0](https://github.com/unity-sds/app-pack-generator/releases/tag/0.1.0)
- [unity-app-generator](https://github.com/unity-sds/unity-app-generator) : [0.1.0](https://github.com/unity-sds/unity-app-generator/releases/tag/0.1.0)
- [unity-example-application](https://github.com/unity-sds/unity-example-application) : [0.1.0](https://github.com/unity-sds/unity-example-application/releases/tag/0.1.0)
- [unity-py](https://github.com/unity-sds/unity-py) : [0.2.0](https://github.com/unity-sds/unity-py/releases/tag/0.2.0)
- [sounder-sips-tutorial](https://github.com/unity-sds/sounder-sips-tutorial) : [0.2.0](https://github.com/unity-sds/sounder-sips-tutorial/releases/tag/0.2.0)


### Added

#### Development Environment
* [unity-ads-deployment #73](https://github.com/unity-sds/unity-ads-deployment/issues/73) Build Unity Application Package Generator
* [unity-cs #129](https://github.com/unity-sds/unity-cs/issues/129) Add custom JupyterHub Authenticator to pass Cognito tokens from JupyterHub to JupyterLab
* [unity-ads-deployment #79](https://github.com/unity-sds/unity-ads-deployment/issues/79) Add Dockstore API access to Unity.py
* [unity-ads-deployment #78](https://github.com/unity-sds/unity-ads-deployment/issues/78) Build and deploy Jupyter stacks automatically

#### Application Registry
* [unity-ads-deployment #80](https://github.com/unity-sds/unity-ads-deployment/issues/80) Create a simple Docker project pipeline for testing the Gitlab Docker executor
* [unity-ads-deployment #74](https://github.com/unity-sds/unity-ads-deployment/issues/74) Parameterize Dockstore Deployment
* [unity-ads-deployment #39](https://github.com/unity-sds/unity-ads-deployment/issues/39) Document Dockstore Deployment
* [unity-ads-deployment #87](https://github.com/unity-sds/unity-ads-deployment/issues/87) Convert Unity.py Application Package API to use Hosted Workflows

#### CI/CD

* [unity-ads-deployment #90](https://github.com/unity-sds/unity-ads-deployment/issues/90) Create a simple Gitlab project to trigger building other projects
* [unity-ads-deployment #99](https://github.com/unity-sds/unity-ads-deployment/issues/99) Add MCP Gitlab runner deployment scripts to Github

### Fixed

#### Application Registry

* [unity-ads-deployment #102](https://github.com/unity-sds/unity-ads-deployment/issues/102) Modify Dockstore to use latest AMI
