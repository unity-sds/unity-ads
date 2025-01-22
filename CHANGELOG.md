# Changelog

All notable changes for the Unity Application Development Serves will be documented in this file. This combines changes across multiple repositories.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

--------

## [Unity Release 24.3 - 24.4] - 2025-01-22

### Repository Tags

- [unity-ads-deployment](https://github.com/unity-sds/unity-ads-deployment/) : [0.8.0](https://github.com/unity-sds/unity-ads-deployment/releases/tag/0.8.0)
- [unity-docker-stacks](https://github.com/unity-sds/unity-docker-stacks) : [0.2.4](https://github.com/unity-sds/unity-docker-stacks/releases/tag/0.2.4)
- [unity-app-generator](https://github.com/unity-sds/unity-app-generator) : [0.3.2](https://github.com/unity-sds/unity-app-generator/releases/tag/0.3.2)
- [app-pack-generator](https://github.com/unity-sds/app-pack-generator) : [0.4.3](https://github.com/unity-sds/app-pack-generator/releases/tag/0.4.3)
- [unity-example-application](https://github.com/unity-sds/unity-example-application) : [0.3.0](https://github.com/unity-sds/unity-example-application/releases/tag/0.3.0)
* [unity-app-build-trigger](https://github.com/unity-sds/unity-app-build-trigger) : [0.2.0](https://github.com/unity-sds/unity-app-build-trigger/tag/0.2.0)

### Jupyter

- [unity-sds/unity-ads-deployment #157](https://github.com/unity-sds/unity-ads-deployment/issues/157) - Add health check endpoint for Jupyterhub
- [unity-sds/unity-ads-deployment #159](https://github.com/unity-sds/unity-ads-deployment/issues/159) - Modify Jupyterhub deployment to front face behind HTTPD (Cloudfront)
- [unity-sds/unity-ads #1](https://github.com/unity-sds/unity-ads/issues/1) - Create JupyterHub unity-marketplace metadata.json
- [unity-sds/unity-ads #4](https://github.com/unity-sds/unity-ads/issues/4) - Test Jupyterhub deployment through marketplace
- [unity-sds/unity-ads #8](https://github.com/unity-sds/unity-ads/issues/8) - [Bug]: Upgrade EKS 1.27 AMIs
- [unity-sds/unity-project-management #170](https://github.com/unity-sds/unity-project-management/issues/170) - Provide ability for U-ADS to use HTTPD with Jupyterhub
- [unity-sds/unity-docker-stacks #9](https://github.com/unity-sds/unity-docker-stacks/issues/9) - Update unity-sds-client to latest version in Unity Data Science docker image

### Application Generation

- [unity-sds/app-pack-generator #22](https://github.com/unity-sds/app-pack-generator/issues/22) - autocatalog: App-pack-gen need to use latest UDS images
- [unity-sds/app-pack-generator #26](https://github.com/unity-sds/app-pack-generator/issues/26) - Remove capture of standard out on papermill notebook runs
- [unity-sds/unity-app-generator #19](https://github.com/unity-sds/unity-app-generator/issues/19) - Fix version tagging in app-pack-generator and unity-app-generator


### Application Auto Build

- [unity-sds/unity-app-build-trigger #10](https://github.com/unity-sds/unity-app-build-trigger/issues/10) - Modify pipeline builder to set umask before installing Github packages
- [unity-sds/unity-project-management #188](https://github.com/unity-sds/unity-project-management/issues/188) - Autocatalog: Generate app-packages with updated app-pack-gen-service
- [unity-sds/unity-project-management #191](https://github.com/unity-sds/unity-project-management/issues/191) - Deploy application build process into shared production venue
- [unity-sds/unity-ads-deployment #165](https://github.com/unity-sds/unity-ads-deployment/issues/165) - Autocatalog: App-pack-gen service upgraded in operations
- [unity-sds/unity-ads-deployment #166](https://github.com/unity-sds/unity-ads-deployment/issues/166) - App-package-gen and unity-app-gen must be pinned to releases not the main branch
- [unity-sds/unity-ads-deployment #167](https://github.com/unity-sds/unity-ads-deployment/issues/167) - Update application builder (CI/CD) deployment process documentation
- [unity-sds/unity-ads-deployment #168](https://github.com/unity-sds/unity-ads-deployment/issues/168) - Modify application build process with selectable unity-app-generator versions
- [unity-sds/unity-ads-deployment #169](https://github.com/unity-sds/unity-ads-deployment/issues/169) - Tag Gitlab runners and jobs to allow running of build process in the appropriate location
- [unity-sds/unity-ads-deployment #171](https://github.com/unity-sds/unity-ads-deployment/issues/171) - Improve application build process to redeploy API gateway without destroying stage
- [unity-sds/unity-ads-deployment #173](https://github.com/unity-sds/unity-ads-deployment/issues/173) - [Bug]: Update deployed app-pack-gen services to use newest version.
- [unity-sds/unity-ads-deployment #175](https://github.com/unity-sds/unity-ads-deployment/issues/175) - Update ci_cd README with current deployment steps
- [unity-sds/unity-ads-deployment #176](https://github.com/unity-sds/unity-ads-deployment/issues/176) - Permission error in APGS Built Applicaiton Pacakges


--------

## [Unity Release 23.3 - 24.2] - 2024-07-03

### Repository Tags

- [unity-ads-deployment](https://github.com/unity-sds/unity-ads-deployment/) : [0.6.0](https://github.com/unity-sds/unity-ads-deployment/releases/tag/0.6.0)
- [unity-docker-stacks](https://github.com/unity-sds/unity-docker-stacks) : [0.2.3](https://github.com/unity-sds/unity-docker-stacks/releases/tag/0.2.3)
- [app-pack-generator](https://github.com/unity-sds/app-pack-generator) : [0.3.0](https://github.com/unity-sds/app-pack-generator/releases/tag/0.3.0)
- [unity-app-generator](https://github.com/unity-sds/unity-app-generator) : [0.3.0](https://github.com/unity-sds/unity-app-generator/releases/tag/0.3.0)
- [unity-example-application](https://github.com/unity-sds/unity-example-application) : [0.3.0](https://github.com/unity-sds/unity-example-application/releases/tag/0.3.0)
* [unity-app-build-trigger](https://github.com/unity-sds/unity-app-build-trigger) : [0.1.0](https://github.com/unity-sds/unity-app-build-trigger/tag/0.1.0)

### Development Environment

- [unity-sds/unity-ads-deployment #119](https://github.com/unity-sds/unity-ads-deployment/issues/119) - Set up common Terraform script for U-ADS cost allocation tags (23.3)
- [unity-sds/unity-ads-deployment #111](https://github.com/unity-sds/unity-ads-deployment/issues/111) - Move custom Cognito access tokens class out of JupyterHub config and into a separate file (23.3)
- [unity-sds/unity-docker-stacks #4](https://github.com/unity-sds/unity-docker-stacks/issues/4) - Preserve Conda environment in Jupyterlab through restarts (23.3)
- [unity-sds/unity-docker-stacks #3](https://github.com/unity-sds/unity-docker-stacks/issues/3) - Install Unity-py in Jupyter ADE (23.3)
- [unity-sds/unity-ads-deployment #112](https://github.com/unity-sds/unity-ads-deployment/issues/112) - Apply cost tags Jupyerlab (23.3)
- [unity-sds/app-pack-generator #8](https://github.com/unity-sds/app-pack-generator/issues/8) - Update stage-out to use U-DS stage-out version 5.2.1 (23.3)
- [unity-sds/unity-example-application #4](https://github.com/unity-sds/unity-example-application/issues/4) - Update notebook testing to reflect changes to app-pack-generator update to U-DS 5.2.1 (23.3)
- [unity-sds/app-pack-generator #12](https://github.com/unity-sds/app-pack-generator/issues/12) - Update to use U-DS 5.2.2 (23.3)
- [unity-sds/app-pack-generator #13](https://github.com/unity-sds/app-pack-generator/issues/13) - Modify papermill to use jovyan home directory as execution context (23.3)
- [unity-sds/app-pack-generator #11](https://github.com/unity-sds/app-pack-generator/issues/11) - Convert app-pack-generator to use PEP 621 package metadata (23.3)
- [unity-sds/app-pack-generator #16](https://github.com/unity-sds/app-pack-generator/issues/16) - Application Package workflows should have the output of stage-out  (23.3)
- [unity-sds/app-pack-generator #17](https://github.com/unity-sds/app-pack-generator/issues/17) - Allow for EDL_PASSWORD type at the stage-in to be modified at run time (non hardcoded) (23.3)
- [unity-sds/app-pack-generator #15](https://github.com/unity-sds/app-pack-generator/issues/15) - Seperate CWL generation logic from application parsing logic (23.3)
- [unity-sds/unity-app-generator #15](https://github.com/unity-sds/unity-app-generator/issues/15) - Convert unity-app-generator to use PEP 621 package metadata (23.3)
- [unity-sds/unity-ads-deployment #96](https://github.com/unity-sds/unity-ads-deployment/issues/96) - Bring test deployment setup in sync with dev deployment (23.3)
- [unity-sds/unity-ads-deployment #145](https://github.com/unity-sds/unity-ads-deployment/issues/145) - Seperate Jupyterhub Cognito setup into a seperate step allowing for cross venue setup (23.3)
- [unity-sds/unity-ads-deployment #61](https://github.com/unity-sds/unity-ads-deployment/issues/61) - Review and update Jupyterlab deployment documentation (24.1)
- [unity-sds/unity-ads-deployment #148](https://github.com/unity-sds/unity-ads-deployment/issues/148) - Fix unity_auth.py to work with latest verison of Jupyter (24.1)
- [unity-sds/unity-ads-deployment #146](https://github.com/unity-sds/unity-ads-deployment/issues/146) - Convert JupyterHub deployment to use EKS module instead of individual resources (24.1)
- [unity-sds/unity-ads-deployment #147](https://github.com/unity-sds/unity-ads-deployment/issues/147) - Use RBAC instead of kube2iam to access S3 buckets within Jupyterhub (24.1)
- [unity-sds/unity-ads-deployment #129](https://github.com/unity-sds/unity-ads-deployment/issues/129) - Modify JupyterHub to use U-CS variables and SSM parameters (24.1)
- [unity-sds/unity-ads-deployment #151](https://github.com/unity-sds/unity-ads-deployment/issues/151) - Create script to save Kubernetes configuration of Jupyter user EBS claims (24.1)
- [unity-sds/unity-ads-deployment #149](https://github.com/unity-sds/unity-ads-deployment/issues/149) - Add scripts to the Jupyterhub deployment to allow restoring user claims between clean redeployments (24.1)
- [unity-sds/unity-ads-deployment #150](https://github.com/unity-sds/unity-ads-deployment/issues/150) - Create scripts to enable backing up Jupyterhub user EBS volumes to Snapshots and restoring them (24.1)
- [unity-sds/app-pack-generator #20](https://github.com/unity-sds/app-pack-generator/issues/20) - Update stage-in, stage-out versions and environments to support new STAC metadata requirements (24.1)
- [unity-sds/unity-ads-deployment #154](https://github.com/unity-sds/unity-ads-deployment/issues/154) - Deploy configuration into user environments to make Conda default to the user's home directory (24.1)

### CI/CD

- [unity-sds/unity-app-generator #7](https://github.com/unity-sds/unity-app-generator/issues/7) - Create Gitlab Project YML to call unity-app-generator (23.3)
- [unity-sds/unity-app-generator #14](https://github.com/unity-sds/unity-app-generator/issues/14) - Update Git cloning tool to add YML into repo and push to Gitlab (23.3)
- [unity-sds/unity-ads-deployment #47](https://github.com/unity-sds/unity-ads-deployment/issues/47) - Configure Gitlab to Build and Deliver an Example Algorithm (23.3)
- [unity-sds/unity-app-build-trigger #1](https://github.com/unity-sds/unity-app-build-trigger/issues/1) - Create an API endpoint to push foreign Git repositories into Gitlab to trigger automated application building (24.1)
- [unity-sds/unity-app-build-trigger #5](https://github.com/unity-sds/unity-app-build-trigger/issues/5) - Document app build automation pipeline (24.1)
- [unity-sds/unity-app-build-trigger #6](https://github.com/unity-sds/unity-app-build-trigger/issues/6) - Fix error that occurs when the app build pipeline pushes into a repo already existing into Gitlab (24.1)
- [unity-sds/unity-app-build-trigger #4](https://github.com/unity-sds/unity-app-build-trigger/issues/4) - Modify automation pipeline such that can be used with keys per subgroup (24.1)
- [unity-sds/unity-ads-deployment #162](https://github.com/unity-sds/unity-ads-deployment/issues/162) - Add JWT Python package to app build Lambda function (24.2)
- [unity-sds/unity-ads-deployment #153](https://github.com/unity-sds/unity-ads-deployment/issues/153) - Automate pipeline application building lambda and api gateway deployment (24.2)
- [unity-sds/unity-ads-deployment #164](https://github.com/unity-sds/unity-ads-deployment/issues/164) - Fix permission issues related to MCP Gitlab upgrade (24.2)
- [unity-sds/unity-ads #7](https://github.com/unity-sds/unity-ads/issues/7) - Deploy app build pipeline to test and prod shared environments (24.2)

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
