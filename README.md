# Stable Diffusion WebUI Initializer

Welcome to the **Stable Diffusion WebUI Initializer** repository! This repository provides tools to easily initialize and manage the Stable Diffusion WebUI. With the included `Makefile`, you can quickly start the WebUI, launch it in different modes, or initialize it with a single command.

---

## 🛠 **Features**

- **Simple Initialization**: Use the `Makefile` to easily initialize the WebUI environment.
- **WebUI Launch Options**: Start the WebUI with or without a frontend, depending on your requirements.
- **API Access**: Enable API access for integration with other applications.
- **Custom Port**: Configure the WebUI to run on your desired port.

---

## 📦 **Installation**

1. **Clone the Repository**

First, clone this repository and the Stable Diffusion WebUI repository:

```bash
git clone git@github.com:Abdelmathin/stable-diffusion-webui-initializer.git
cd stable-diffusion-webui-initializer
```

2. **Set Up Dependencies**

Make sure to install all required dependencies. If there are any Python package dependencies, install them using:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

You can use the provided `Makefile` to run various tasks.

### Start the WebUI

To start the WebUI in the parent `stable-diffusion-webui` directory:

```bash
make start
```


