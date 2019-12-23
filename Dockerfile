FROM python:3

ADD combine_3D_objects.py /

CMD [ "python", "./combine_3D_objects.py" ]