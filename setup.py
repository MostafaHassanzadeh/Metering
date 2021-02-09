import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Metering-Project-MostafaHassanzadeh", # Replace with your own username
    version="0.0.1",
    author="Mostafa Hassanzadeh And Hamidreza Miryazdi",
    author_email="mostafaa.hasanzadeh@gmail.com",
    description="Metering",
    long_description="Power_grid_energy_measurement_and_monitoring_system",
    long_description_content_type="text/markdown",
    url="https://github.com/MostafaHassanzadeh/Metering",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.1',
)