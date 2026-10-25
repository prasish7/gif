# Dino GIF Generator

A small Python script that combines four PNG frames into a looping animated GIF.

## Preview

![Animated dinosaur](dino.gif)

## Requirements

- Python 3.8 or newer
- The [`imageio`](https://pypi.org/project/imageio/) package

## Getting started

1. Clone or download this project.
2. Open a terminal in the project directory.
3. Install the dependency:

   ```bash
   python -m pip install imageio
   ```

4. Generate the GIF:

   ```bash
   python gif.py
   ```

The script reads `dino1.png`, `dino2.png`, `dino3.png`, and `dino4.png`, then creates or replaces `dino.gif` in the same directory.

## How it works

The frames are added in filename order and written as an animated GIF with:

- **Frame duration:** 500 milliseconds
- **Looping:** Infinite

To change the animation speed or frame order, edit `gif.py`:

```python
iio.imwrite("dino.gif", images, duration=500, loop=0)
```

## Project structure

```text
.
├── gif.py       # Creates the animated GIF
├── dino.gif     # Generated animation
├── dino1.png   # Frame 1
├── dino2.png   # Frame 2
├── dino3.png   # Frame 3
└── dino4.png   # Frame 4
```

## Notes

- Keep all input PNG files in the same directory as `gif.py`.
- Run the script from the project directory so the relative file paths resolve correctly.
- Re-running the script updates `dino.gif` with the current PNG frames.