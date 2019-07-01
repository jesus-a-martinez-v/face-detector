# Face Detector

Simple face detector implemented using OpenCV's Haar Cascades.


## Installation

I recommend you have `virtualenv` installed. After that, create a new environment and activate it:

```bash
$> virtualenv -p python3 venv
$> source venv/bin/activate
```

After that, just install the requirements:

```bash
pip install -r requirements.txt
```

## Try it

At the root of the project, execute the following command to get a taste of how it works:

```bash
python detect_faces.py --face cascades/haarcascade_frontalface_default.xml --image images/obama.png
```

You'll get a result like this:

![Obama's face](http://datasmarts.net/wp-content/uploads/2019/05/obama.png)
