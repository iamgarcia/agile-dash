# Agile Project Dashboard

## Setup
The following setup process is intended for Ubuntu OS.

1. Update system
    * Get updated software list `sudo apt update`
    * Apply updates `sudo apt upgrade`

2. Install latest version of Python 3
    * Check if you have Python 3 already installed by running
        `python3 --version`. If Python 3 was not detected, continue
        with the Python 3 installation process.
    * Install Python 3 by running `sudo apt-get install python3.10`. Note that
        Python 3.10 is the minimum recommended version because the project
        was developed using version 3.10. Using a version less than 3.10 may
        result in the project not running as intended.
    * Verify the Python 3 installation by running
        ```shell
        $ which python3
        $ python3 --version
        ```

3. Install Python package manager
    * Install pip3
        ```shell
        $ sudo apt install python3-pip
        ```
    * Verify the pip3 installation by running
        ```shell
        $ which pip3
        ```

4. Clone repository by running `git clone ___blank___`

5. Create virtual environment
    * Using the terminal, navigate to the project directory.
        ```shell
        $ cd agile-project-dashboard
        ```
    * Create a virtual environment in the project directory.
        ```shell
        $ python3 -m venv ./venv
        ```
    * Activate the newly created virtual environment.
        ```shell
        $ source venv/bin/activate
        ```

6. Install project dependencies
    ```shell
    $ pip3 install -r requirements.txt
    ```
