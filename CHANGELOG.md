# Changelog

All notable changes for the Unity Application Development Serves will be documented in this file. This combines changes across multiple repositories.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

--------

## [Unity Release 23.2] - 2023-07-17

### Repository Tags

- [unity-ads-deployment](https://github.com/unity-sds/unity-ads-deployment/) : [0.4.0](https://github.com/unity-sds/unity-ads-deployment/releases/tag/0.4.0)
- [unity-docker-stacks](https://github.com/unity-sds/unity-docker-stacks) : [0.1.0](https://github.com/unity-sds/unity-docker-stacks/releases/tag/0.1.0)
- [app-pack-generator](https://github.com/unity-sds/app-pack-generator) : [0.2.0](https://github.com/unity-sds/app-pack-generator/releases/tag/0.2.0)
- [unity-app-generator](https://github.com/unity-sds/unity-app-generator) : [0.2.0](https://github.com/unity-sds/unity-app-generator/releases/tag/0.2.0)
- [unity-example-application](https://github.com/unity-sds/unity-example-application) : [0.2.0](https://github.com/unity-sds/unity-example-application/releases/tag/0.2.0)
- [unity-py](https://github.com/unity-sds/unity-py) : [0.1.2](https://github.com/unity-sds/unity-py/releases/tag/0.1.2)
- [sounder-sips-tutorial](https://github.com/unity-sds/sounder-sips-tutorial) : [0.2.0](https://github.com/unity-sds/sounder-sips-tutorial/releases/tag/0.2.0)

### Added

#### Development Environment

- [unity-sds/app-pack-generator #1](https://github.com/unity-sds/app-pack-generator/issues/1) - Modify app-pack-generator to use U-DS STAC based stage in and stage out
- [unity-sds/app-pack-generator #2](https://github.com/unity-sds/app-pack-generator/issues/2) - Provide example CWL files that call U-DS stage in/out Docker images
- [unity-sds/app-pack-generator #4](https://github.com/unity-sds/app-pack-generator/issues/4) - Modify GitHelper to support more use case other than remote URL cloning only, support local repos
- [unity-sds/app-pack-generator #5](https://github.com/unity-sds/app-pack-generator/issues/5) - Allow optional arguments in generated CWL files so that they do not need to be supplied in a cwltool call
- [unity-sds/app-pack-generator #10](https://github.com/unity-sds/app-pack-generator/issues/10) - Update app-pack-generator README for release
- [unity-sds/unity-app-generator #13](https://github.com/unity-sds/unity-app-generator/issues/13) - Modify build_ogc_app.py to break process into independent steps that can be run independently
- [unity-sds/unity-app-generator #4](https://github.com/unity-sds/unity-app-generator/issues/4) - Integrate unity-app-generator script into Gitlab
- [unity-sds/unity-app-generator #5](https://github.com/unity-sds/unity-app-generator/issues/5) - Integrate Dockstore API into unity-app-generator
- [unity-sds/unity-app-generator #6](https://github.com/unity-sds/unity-app-generator/issues/6) - Integrate Docker registry push into unity-app-generator
- [unity-sds/unity-app-generator #8](https://github.com/unity-sds/unity-app-generator/issues/8) - Modify unity-app-generator to create Dockstore.cwl that calls main workflow CWL
- [unity-sds/unity-app-generator #9](https://github.com/unity-sds/unity-app-generator/issues/9) - Add command line options to unity-app-generator to optionally push docker image into a registry
- [unity-sds/unity-app-generator #16](https://github.com/unity-sds/unity-app-generator/issues/16) - Update unity-app-generator README for release
- [unity-sds/unity-example-application #1](https://github.com/unity-sds/unity-example-application/issues/1) - Rewrite example notebook to use updated stage_in/stage_out mechanism of unity-app-generator.
- [unity-sds/unity-example-application #2](https://github.com/unity-sds/unity-example-application/issues/2) - Use unity-py in example notebook for input and output of STAC files for stage-in and stage-out
- [unity-sds/unity-example-application #3](https://github.com/unity-sds/unity-example-application/issues/3) - Update unity-example-notebook README for release

#### Application Registry

- [unity-sds/unity-ads-deployment #113](https://github.com/unity-sds/unity-ads-deployment/issues/113) - Apply cost tags to Dockstore
- [unity-sds/unity-ads-deployment #89](https://github.com/unity-sds/unity-ads-deployment/issues/89) - Verify Dockstore database can be restored after rebuild
- [unity-sds/unity-py #30](https://github.com/unity-sds/unity-py/issues/30) - Add Dockstore API interface for retrieving application files
- [unity-sds/unity-py #34](https://github.com/unity-sds/unity-py/issues/34) - Add upload of multiple files at one to Dockstore unity.py interface

#### CI/CD

- [unity-sds/unity-app-generator #3](https://github.com/unity-sds/unity-app-generator/issues/3) - Automate MCP Gitlab Project Creation using Gitlab API
- [unity-sds/unity-ads-deployment #107](https://github.com/unity-sds/unity-ads-deployment/issues/107) - Deploy unity-app-generator into Gitlab runner Terraform scripts

#### Container Registry

- [unity-sds/unity-ads-deployment #100](https://github.com/unity-sds/unity-ads-deployment/issues/100) - Deploy a Docker container registry system


### Fixed

#### Development Environment
- [unity-sds/app-pack-generator #3](https://github.com/unity-sds/app-pack-generator/issues/3) - Add missing requirement "giturlparse>=0.10.0" to setup.py file.
- [unity-sds/unity-app-generator #2](https://github.com/unity-sds/unity-app-generator/issues/2) - Repo2Docker build error when attempting to generate application package


--------

## [Unity Release 23.1] - 2023-04-07

### Repository Tags

- [unity-ads-deployment](https://github.com/unity-sds/unity-ads-deployment/) : [0.3.0](https://github.com/unity-sds/unity-ads-deployment/releases/tag/0.3.0)
- [unity-docker-stacks](https://github.com/unity-sds/unity-docker-stacks) : [0.1.0](https://github.com/unity-sds/unity-docker-stacks/releases/tag/0.1.0)
- [app-pack-generator](https://github.com/unity-sds/app-pack-generator) : [0.1.0](https://github.com/unity-sds/app-pack-generator/releases/tag/0.1.0)
- [unity-app-generator](https://github.com/unity-sds/unity-app-generator) : [0.1.0](https://github.com/unity-sds/unity-app-generator/releases/tag/0.1.0)
- [unity-example-application](https://github.com/unity-sds/unity-example-application) : [0.1.0](https://github.com/unity-sds/unity-example-application/releases/tag/0.1.0)
- [unity-py](https://github.com/unity-sds/unity-py) : [0.1.0](https://github.com/unity-sds/unity-py/releases/tag/0.1.0)
- [sounder-sips-tutorial](https://github.com/unity-sds/sounder-sips-tutorial) : [0.1.0](https://github.com/unity-sds/sounder-sips-tutorial/releases/tag/0.1.0)


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
