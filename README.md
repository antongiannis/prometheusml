<div style="margin-bottom:2rem;"></div>
<div align="center">

  <picture>
    <source height="150" media="(prefers-color-scheme: dark)" srcset="https://yailab.com/assets/logo/logo-prometheus-white.svg">
    <source height="150" media="(prefers-color-scheme: light)" srcset="https://yailab.com/assets/logo/logo-prometheus-black.svg">
    <img height="150" alt="Shows PrometheusML logo" src="https://yailab.com/assets/logo/logo-prometheus-black.svg">
  </picture>

</div>

-----------------
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![MIT License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

Prometheus<span style="color: #ff7F2a;">ML</span> Core is an open-source no-code platform for building machine learning 
and deep learning models developed by [yaiLab](https://yailab.com/).   

## What exactly is Prometheus<span style="color: #ff7F2a;">ML</span> and Prometheus<span style="color: #ff7F2a;">ML</span> Core?

There are two versions of Prometheus<span style="color: #ff7F2a;">ML</span>:
- The open-source Prometheus<span style="color: #ff7F2a;">ML</span> Core
- The cloud data science assitant Prometheus<span style="color: #ff7F2a;">ML</span>

Prometheus<span style="color: #ff7F2a;">ML</span> Core allows anyone and everyone to build machine learning models in an
interactive way through a UI, whilst Prometheus<span style="color: #ff7F2a;">ML</span> is a cloud data science assitant that helps
users build specialised machine learning models fast in physics-intense fields.

## Is it free?

Yes, Prometheus<span style="color: #ff7F2a;">ML</span> Core is completely free. You can use Prometheus<span style="color: #ff7F2a;">ML</span> Core for free by following the instalation steps
in this [repo](#install-prometheusml).

Alternatively, to try out the cloud data science assistant Prometheus<span style="color: #ff7F2a;">ML</span> on a **free** trial go to our website and press on 
[Try it now!](https://yailab.com). You can also find more info on the data science assitant 
Prometheus<span style="color: #ff7F2a;">ML</span> [here](https://yailab.com/product.html).

## How does Prometheus<span style="color: #ff7F2a;">ML</span> Core work?

Prometheus<span style="color: #ff7F2a;">ML</span> Core will help you build an entire machine learning pipeline without 
writing a single of code by guiding you through the entire process.  

### 1. Data upload and evaluation
- gif/video 1
### 2. Feature engineering 
- gif/video 2
### 3. Algorithm selection 
- gif/video 3
### 4. Model validation and deployment 
- gif/video 4
### 5. Making predictions
- gif/video 5

## Canonical source

The canonical source of Prometheus<span style="color: #ff7F2a;">ML</span> where all development takes place is 
[hosted on GitLab.com](https://gitlab.com/yailab/prometheusml).

## Table of contents

* [Install PrometheusML](#install-prometheusml)
* [Documentation](#documentation)
* [Discussion on AI ethics](#discussion-on-ai-ethics)
* [Contributing](#contributing-to-prometheusml)
* [Bugs and feature requests](#bugs-and-feature-requests)
* [License and Copyright](#copyright-and-license)
* [Community](#community)


## Install PrometheusML
Install Prometheus<span style="color: #ff7F2a;">ML</span> on Docker Swarm with the cloud native Docker Compose tool. 
You need to follow the next steps.

**_Important consideration_**. The default Docker Compose configuration is not intended for production. It creates 
a proof of concept (PoC) implementation where all Prometheus<span style="color: #ff7F2a;">ML</span> services are placed 
into a cluster.

### 1. Environment setup
Before proceeding to using Prometheus<span style="color: #ff7F2a;">ML</span>, you need to prepare your environment.

You need to have Docker Compose **installed** on your computer. Docker Compose relies on Docker Engine, 
so make sure you have Docker Engine installed either locally or remote, depending on your setup. More details on how 
to install it can be found in the [Docker Compose documentation](https://docs.docker.com/compose/install/).

### 2. Clone repository
```sh 
git clone https://gitlab.com/yailab/prometheusml.git
```

### 3. Launch PrometheusML
Go to the cloned repository folder, and type the following commands:

```sh
# Set needed environment variable(s)
export gl_username="yailab" prometheus_dir="/home/prometheus/prometheusml" 
# Run the containers and bind your local repo to them
docker compose up -d --remove-orphans
```

You can now access Prometheus<span style="color: #ff7F2a;">ML</span> from the browser of your choice 
by typing the address `localhost:5000`. 

You can create **a new user** by going to the registration page of your locally launched 
Prometheus<span style="color: #ff7F2a;">ML</span> instance. The created user comes preloaded 
with two **templates**, a general _regression_ and a _classification_ one. You can now 
<span style="color: #ff7F2a;">enjoy building machine learning models</span>!


## Documentation
The documentation of Prometheus<span style="color: #ff7F2a;">ML</span> is under 
<span style="color: #ff7F2a;">active development</span>! 

You can start with the following **tutorial videos** for a quick introduction:
- [Using PrometheusML to predict ...]()
- [Using PrometheusML to classify ...]()


## Discussion on AI ethics
At y<span style="color: #ff7F2a;">ai</span>Lab we **democratise** AI and believe in responsible AI use. Whilst we are super excited about AI’s 
ability to help humanity with its biggest problems, we are committed to **Ethical** and **Responsible** AI. 

What we do can potentially affect everyone... and the responsibility ... We strongly believe in transparency and inclusive dicsussion ..
We need the community's help to ... Join our [Discord channel]() and join the discussion to shape... 


## Contributing to PrometheusML
Prometheus<span style="color: #ff7F2a;">ML</span> is an open source project, and we are 
very happy to accept community contributions. Please refer to the [Contributing guide](CONTRIBUTING.md) 
for more details.

### Code of Conduct

Everyone participating in the Prometheus<span style="color: #ff7F2a;">ML</span> project, and in particular in the issue tracker,
pull requests, and social media activity, is expected to treat other people with respect
and more generally to follow the guidelines articulated in the
[Community Code of Conduct](CODE_OF_CONDUCT.md).

At the same time, we don't take ourselves too seriously and humor is encouraged. We are not savages.

### Versioning

This project is maintained under the [Semantic Versioning guidelines](https://semver.org/).

See the [Releases section](https://gitlab.com/yailab/prometheusml/-/releases) of our GitLab project for 
changelogs for each release version of Prometheus<span style="color: #ff7F2a;">ML</span>.


## Copyright and license

Code and documentation copyright 2022 yaiLab, Ltd.

See the [LICENSE](LICENSE) file for licensing information as it pertains to
files in this repository.

Code released under the [MIT license](). ??


## Community

* Follow [@lab_yai](https://twitter.com/lab_yai) on Twitter for the latest yaiLab news, or 
sign up for our [newsletter]().
* If you want to chat and connect, join our [Discord community]()!