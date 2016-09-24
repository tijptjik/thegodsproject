# Pelican : thegodsproject.com

## Installation

### Clone Repo & Submodules from Github
```
git clone git@github.com:tijptjik/thegodsproject.git && cd thegodsproject
git submodule update --init --recursive
```

### Install python dependencies
```
conda env create -n thegodsproject -f environment.yml
source activate thegodsproject
```
**NOTE** : You should always run `source activate thegodsproject` when running the pelican project locally as it activated the conda environment with all the python dependencies in it.

## Project Structure

```bash
thegodsproject
|-- content # Markdown posts for the blog
|   `-- extra # Misc files - explicitly mapped to output in pelicanconf.py
|-- develop_server.sh
|-- environment.yml # Conda Environement with Python Dependencies
|-- nest # theme
|   `-- static # CSS and fonts
|   `-- templates # HTML jinja templates 
|-- Makefile # Make Tasks
|-- pelicanconf.py # Main config
|-- plugins # Submodules - don't edit
|-- publishconf.py # Config file with additional settings for production
`-- readme.md # You are here
```


### Config Files

So based on the project structure, the config is managed by :

* `pelicanconf.py`
* `publishconf.py`

## Site Development

Site development isdone following the conventions for `Pelican` [themes](http://docs.getpelican.com/en/3.6.3/themes.html) which uses [Jinja](http://jinja.pocoo.org/docs/dev/) for its templates.

The Jinja templates are located at `nesttemplates`. Inspect the following three Jinja templates to get an idea of the site structure:

```bash
nest/templates/base.html # All pages should extend the base template
nest/templates/index.html # The landing page
nest/templates/article.html # Basis for all articles
```

### Tasks

From the project root

#### Generation for Development

```bash
make html
```

#### Live Reload

```bash
make regenerate
```

#### Web Server with Live Reload

```bash
./develop_server.sh start # generate & run server
./develop_server.sh stop # stop backgrounded server
# or
make devserver
```

#### Publish to Github Pages

```bash
make github
```


#### Config Options

* [Available Markdown Extensions](http://pythonhosted.org/Markdown/extensions/)
* [Available Pelican Plugins](https://github.com/getpelican/pelican-plugins#pelican-plugins)