# BP-Django-Test
This is an example repository created directly from a **django** template.
This repository is a comprehensive example of production **REST API** with database and admin page,
which is deployed on multiple environments.
***
### Local environment
Create **.env** file:

| **Variable**              | **Description**            | **Value**                                          |
|---------------------------|----------------------------|----------------------------------------------------|
| _PROJECT                  | Project name               | BP-Test-Django                                     |
| _USER                     | User name                  | Filip-231                                          |
| ALLOWED_HOSTS             | The host that Django allow | 0.0.0.0                                            |
| SECRET_KEY                | Random Django secret key   | bbb6c33k+68m1awa+dzeadaczaalycda3bk2ev=nsx=-1ai3i0 |
| DJANGO_SUPERUSER_PASSWORD | Password to login          | password                                           |
| DJANGO_SUPERUSER_USERNAME | Admin user name            | admin                                              |
| DJANGO_SUPERUSER_EMAIL    | Admin e-mail               | admin@example.com                                  |

Install all necessary packages: `make install`.
Up the composition: `make up`, login on admin page `http://localhost:8020/admin`, down the composition: `make down`.
***
## Repository secrets
Navigate to GitHub Actions secrets [tab](https://github.com/Filip-231/BP-Test-Django/settings/secrets/actions).

| **Variable**               | **Description**                                                                                                | **Example Value**                                  |
|----------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| TESTING_HOST_IP            | IP address of your testing linux instance                                                                      | 192.168. 1.1                                       |
| TESTING_SSH_PRIVATE_KEY    | Private ssh key which is needed to make ssh tunel to testing instance. Generated from cloud UI.                | -----BEGIN RSA PRIVATE KEY-----                    |
| PRODUCTION_HOST_IP         | IP address of your production linux instance.                                                                  | 192.168. 1.1                                       |
| PRODUCTION_SSH_PRIVATE_KEY | Private ssh key which is needed to make ssh tunel to prod instance. Generated from cloud UI.                   | -----BEGIN RSA PRIVATE KEY-----                    |
| SSH_PRIVATE_KEY_TO_REPO    | This is ssh key of an instance which has access to private repositories. Is generated with key-gen.            | -----BEGIN RSA PRIVATE KEY-----                    |
| PERSONAL_ACCESS_TOKEN      | PAT generated in GitHub developers menu, [token](https://github.com/settings/tokens) used to get package image | ghp_ ........                                      |
| DJANGO_SECRET_KEY          | Django secret key consisting multiple characters.                                                              | a7g1no9a2dhcosard72(ale66u5pg4stf9#b97maiccou6sekk |
| DJANGO_SUPERUSER_PASSWORD  | Password for admin account                                                                                     | password                                           |

I encourage You to make 2 separate environments for testing and production, then create a specific environment variables.

To configure new environment:
https://github.com/Filip-231/BP-Test-Django/settings/environments/new

In GitHub You can add a protection rule with reviewer, but the repository need to be visible.

***
## Features
After installing local environment `. .venv/bin/activate` and `make help` to see help message.
```
all                 commit and push all changes
brew-allure         install allure with brew long
build               build docker-compose image
bump                (PART= ) bump the release version - deduced automatically from commit messages unless PART is provided
changelog           (UNRELEASED= current version) update the changelog incrementally.
check-commit        check the commit message is valid
clean               clean up temp and trash files
commit              make interactive conventional commit
docker-build-dev    build docker image locally
docker-download-package (VERSION= specifies version) download package from GH package registry
docker-exec         exec in a docker container
docker-run-dev      run docker image including .env file
docker-run-package  (VERSION= ) runs package downloaded from GH package registry
docs                render documentation
down                down the compose
down-volumes        remove docker images and volumes
format              format code
freeze              (UPGRADE= ) generate requirements from setup.cfg
get-version         output the current version
git                 reset git, specify new project and git user
help                display this help message
init                (LANGUAGE=django/tool/dbt) create cruft project and install pre-requirements
install             install all requirements
lint                run static code checkers
pre-install         install pre-requirements
release             create a new github release
set-project-name    (_PROJECT=project _USER=user ) set initial environment
tag                 pull tags and tag a new version
test                (ALLURE=True BROWSE=True) run tests
up                  (ALLOWED_HOSTS= SECRET_KEY= ) up the compose
update-makefiles    update configuration files
update-project      update cruft project and install pre-requirements
update              update cruft project and configuration files
venv                install virtual environment

```

All these commands are used to effectively manage the django project.
***
## Continuous Integration and delivery
Complete CI-CD process will be visible in GitHub Actions [page](https://github.com/Filip-231/BP-Test-Django/actions) containing:
* **CI** - run on every push to master and on pull requests.
  * Test  - run unit and E2E tests.
  * Format - checks if code is formatted.
  * Lint - runs all static code checkers with prospector.
  * Docker - build and up docker image.
  * Docker-compose - build and up compose.
* **CD** - manual trigger, automatic deploy to Oracle cloud environment, GH releases and packages.
  * Deploy Testing - deploy to testing environment - linux instance with **TESTING_HOST_IP**.
  * Bump Version - bump current version and push a tag to a repository - after review and approve.
  * Publish Release - publish new release to GitHub [releases](https://github.com/Filip-231/BP-Test-Django/releases).
  * Publish Package - build docker package and push to GitHub [packages](https://github.com/Filip-231?tab=packages&repo_name=BP-Test-Django).
  * Deploy Production - deploy to production - linux instance with IP **PROD_HOST_IP** - after review and approve.
* **CI/CD** - manual trigger, includes CI and CD pipelines connected.

### CI/CD Pipeline

![CI-CD.png](.github/CI-CD.png)

### Releases
During CD pipeline the new GH release will be created with zipped code, changelog will be updated with new commits pushed master branch, 
tag with a new version will be created.

![Releases.png](.github/Releases.png)

### Packages
The new package with tagged version will be created. 
It can be pulled directly from GH packages with `make docker-download-package` and run `make docker-run-package`.

![Packages.png](.github/Packages.png)

### Unified interactive commits with pre-hook
Pre-hook checks depends on what scope has been changed.

<center>

![Commit.png](.github/Commit.png)

</center>

### Docs
After invoking `make docs` the **sphinx** documentation will be created in public folder. You can open it with a browser.

![Docs.png](.github/Docs.png)

### Allure
You can invoke `make test ALLURE=True BROWSE=True` to make and open allure report with coverage.

![Allure.png](.github/Allure.png)

### Environment Setup
There is **setup.cfg** file which creates list of requirements for: build, dev, lint, test, docs, format, commit.  
To create specified environemt you can run `make install EXTRAS=lint`.
These environments are separated to speed up the CI/CD process, and to include only necessary packages in a final product.
There is a possibility to add a private repository as a custom package (bptestpackage) and install directly in environment. 

To render requirements from setup.cfg run `make freeze` to install dependencies `make install`, to update `make freeze UPGRADE=True`.

<center>
<div style="width: 60%; height: 40%">

![Setup.png](.github/Setup.png)

</div>
</center>

***
## Prerequisites on remote linux instance:

```
sudo apt update
sudo apt upgrade
```

To run this workflow You need to install: `sudo apt install make`

Remember to add ingress rules on your cloud UI- allow all traffic to 8020 port.
`0.0.0.0/0	TCP	All	8000		TCP traffic for ports: 8000`

Nginx:
```
sudo apt install nginx
sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 80 -j ACCEPT
sudo netfilter-persistent save
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
```

SSH:
``` sudo apt install openssh-server```

[Docker installation](https://docs.docker.com/engine/install/ubuntu/)

Docker-compose:
```
sudo apt install curl
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo docker–compose --version
```

GitHub:
```
sudo snap install gh
gh auth login
```


After deploying you can enter admin page on: `http://<IP-to-instance>:8020/admin`

To connect using ssh, generate you ssh key pair and then:
```
chmod 400 ssh-key.key
ssh -i ssh-key.key ubuntu@<IP-to-instance>
```

Pull a package from repo: `docker pull ghcr.io/filip-231/bp-test-django:sha-7abc3b2`
Run a package: `docker run ghcr.io/filip-231/bp-test-django:sha-7abc3b2`
Enter running container: `sudo docker exec -it <container> sh`

***
## Debugging GitHub Actions workflow
If you want to debug GitHub Actions workflow copy and paste this job:
```
      - name: Setup upterm session
        uses: lhotari/action-upterm@v1
```
Then connect from you local machine using ssh:
```
ssh tRrMU4AhXxyn9leHF4vr:ZmZhMJtLmludGVybmFsOjIyMjI=@uptermd.upterm.dev
```
Run `touch continue` when you will find the solution.
