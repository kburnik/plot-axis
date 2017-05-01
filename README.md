# Axis plot drawing

This simple project is used for drawing plot axes with percentage ticks
on an existing rendered image (PNG, BMP, etc.).


## Dev setup (Windows)

* Need to install opencv

```sh
git clone https://github.com/kburnik/plot-axis.git
cd plot-axis
virtualenv env
. venv/Scripts/activate
pip install -r requirements.txt
```


## Sample run

Before running on any image, you need to create a JSON file describing the
top left point of each Y-axis and the height (length) of each axis.

E.g.
```sh
cat <<EOT > graf.png.json
{
  "points": [[15, 25], [15, 448]],
  "lengths": [355, 355]
}
EOT
```

Then simply run it.

```
python draw.py -i graf.png -o out.png
```
