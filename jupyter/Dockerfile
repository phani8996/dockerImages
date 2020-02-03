FROM python:3.5.9-alpine

# Args
ARG WORK_DIR="/usr/src/app"
ARG JUPYTER_PASSWD="tonystark"
ARG JUPYTER_BASE_URL="/jupyter/"
ARG TEMP_CONFIG_FILE="temp_config.txt"

# install jupyter and its dependencies
RUN apk add build-base libzmq musl-dev  zeromq-dev
RUN pip install ipyparallel jupyter
RUN apk del build-base musl-dev  zeromq-dev

# Create required directories and copy files
RUN mkdir -p $WORK_DIR
WORKDIR $WORK_DIR
COPY create_passwd.py $WORK_DIR/

#create jupyter config
RUN jupyter notebook --generate-config
RUN python create_passwd.py $TEMP_CONFIG_FILE $JUPYTER_PASSWD $JUPYTER_BASE_URL
RUN cat $TEMP_CONFIG_FILE >> ~/.jupyter/jupyter_notebook_config.py
RUN ipcluster nbextension enable

# Remove temp file
RUN rm create_passwd.py $TEMP_CONFIG_FILE


CMD ["jupyter", "notebook"]
