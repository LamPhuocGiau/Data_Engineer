# Matplotlib
## Table of contents
- [Chart menu](#Chart-menu)
- [Anatomy of matplotlib code](#Anatomy-of-matplotlib-code)
- [Change line color](#Change-line-color)
- [Add title and legend](#Add-title-and-legend)
- [Adjust and label axes](#Adjust-and-label-axes)
- [Export a chart](#Export-a-chart)

## Chart menu

Chart type | Chart code
---|---
Line chart | plt.plot()
Scatter plot |	plt.scatter()
Bar chart | plt.bar()
Pie chart | plt.pie()
Histogram | plt.hist()

line chart: shows continuous change, often used to measure change over time.

scatterplot: uses position to show the relationship, or correlation, between two numeric values.

bar chart: uses bar height to compare a measure between categorical variables.

pie chart: shows us the breakdown of a whole into its parts.

histogram: shows how one kind of data is distributed.

## Anatomy of matplotlib code

Description | command
---|---
Add a title	| plt.title()
Add a legend | plt.legend()
Add axis labels |	plt.ylabel(), plt.xlabel()
Adjust axes |	plt.xscale(), plt.yticks()
Print graph	| plt.show()

## Change line color

**single-letter color code**.

plt.plot(x, y, color='r').

**full string**.

plt.plot(x, y, color='red').

**hex code**.

plt.plot(x, y, color='#FF0000')

- single-letter color code (8 basic colors).

- full string color (1000+ recognized colors).

- hexadecimal code (any web color).

In addition to color, .plot() will take the parameters linewidth and linestyle. linewidth takes a number that changes the thickness of the line. linestyle takes a string: dotted, dashed, or solid.

```
dashed red line
plt.plot(x, y, color='r', linestyle='dashed')

thick, solid yellow line
plt.plot(x, y, color='yellow', linewidth=5)

thin, dotted white line
plt.plot(x, y, color='#FFFFFF', linewidth=0.5, linestyle='dotted')
```

## Add title and legend

**Add title**.

```
plt.title(‘Effect of Hunger on Mood’)
```
**Add legend**.

- Position the legend: plt.legend() parameter bbox_to_anchor, which takes an (x,y), 0 is the left edge of the graph and 1 is the right edge.

```
plt.plot(x, y, color='red', label='Line Y')
plt.plot(x, z, color='green', label='Line Z')
plt.legend(bbox_to_anchor = (1, 0.5))
```

## Adjust and label axes

**Add label axes**.

```
plt.xlabel(‘Quarter’)
plt.ylabel('Vacuum Cleaner Sales ($)')
```
**Add tick label**.

```
plt.tick_params(axis='x', direction='out', color='red', labelsize='large', labelcolor='purple', labelrotation=30)
```

## Export a chart

```
plt.savefig('my_lineplot.png')
```
Plots will default to .png format, but we can also specify the format as a parameter and save a plot as a .jpeg, .pdf, or .svg file type.

dpi: the number of pixels in the image, or essentially, how big it is.

bbox_inches = 'tight' ensures that our legend, tick labels, and axes aren’t cut off.

```
plt.savefig('my_lineplot.png', dpi=128, bbox_inches='tight')
```

