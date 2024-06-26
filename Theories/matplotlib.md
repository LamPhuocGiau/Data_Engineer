# [Matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html)
## Table of contents
- [Chart menu](#Chart-menu)
- [Anatomy of matplotlib code](#Anatomy-of-matplotlib-code)
- [Change line color](#Change-line-color)
- [Add title and legend](#Add-title-and-legend)
- [Adjust and label axes](#Adjust-and-label-axes)
- [Export a chart](#Export-a-chart)
- [Bar chart](#bar-chart)
- [Scatterplot](#Scatterplot)
- [Subplots](#Subplots)
- [Pie chart](#Pie-chart)
- [Histogram chart](#historgram-chart)
- [AB line](#AB-line)
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
## Bar chart

```
plt.bar(x = data.business_name, height = data.profit, width = 0.8, align = 'center')
plt.title("Profits at 5 Businesses, 2021")
plt.xlabel("Business Name")
plt.ylabel("Profit ($)")
```
x: categorical data for each bar.

height: numeric data to determine the height of each bar.

width: a number we can pass in to set the width of each bar.

align: set to 'center' or 'edge' to align each bar on the x-axis.

**Add error bars**.

```
## make the bar graph
plt.bar(x = data.business_name, height = data.profit, width = 0.8, align = 'center')
plt.title("Profits at 5 Businesses, 2021")
plt.xlabel("Business Name")
plt.ylabel("Profit ($)")

## add the error bars 
plt.errorbar(x = data.business_name, y = data.profit, yerr = data.error_value, fmt='o', color='purple')
```
x and y: restate the X and Y values of the underlying graph.

yerr and/or xerr: set error values in the X or Y direction.

color: set the color of the error bar (optional).

fmt: change the marker.

## Scatterplot

```
plt.scatter(data.tree_age, data.trunk_circumference, color='yellowgreen', alpha=0.5)
plt.title('Effect of Tree Age on Trunk Circumference in Red Oaks')
plt.ylabel('Trunk Circumference (cm)')
plt.xlabel('Tree Age (years)')
plt.show()
```

x and y: the continuous numeric variables to be compared.

color: marker color, as a color code, color name, or hex code.

alpha: marker opacity, as a number between 0 (transparent) and 1 (opaque).

Only x and y are required parameters.

If the points are scattered from bottom-left to top-right in the graph, we’d be able to say “As X increases, Y also increases.” This indicates a positive correlation.

If the points are scattered from top-left to bottom-right in the graph, we’d be able to say “As X increases, Y decreases.” This indicates a negative correlation.

If the points are scattered in a horizontal line, we can say “As X increases, Y remains constant.” This indicates no correlation. A cloud of scattered points with no clear directional grouping also indicates no correlation.

## Subplots

```
plt.suptitle('Rainbow Scatterplots')
plt.subplot(2, 3, 1)
plt.scatter(x, y, color = red)
plt.subplot(2, 3, 2)
plt.scatter(x, y, color = orange)
plt.subplot(2, 3, 3)
plt.scatter(x, y, color = yellow)
plt.subplot(2, 3, 4)
plt.scatter(x, y, color = green)
plt.subplot(2, 3, 5)
plt.scatter(x, y, color = blue)
plt.subplot(2, 3, 6)
plt.scatter(x, y, color = purple)
```
num_rows: number of rows in the grid.

num_columns: number of columns in the grid.

index: the numbered position of the subplot, reading the grid from left-to-right, top-to-bottom.

## Pie chart

```
plt.pie(x = data.donut_vote_count, labels = data.donut_flavor, startangle = 30, colors = ['brown', 'pink', 'purple', 'white', 'red'])
```

x: the numeric variable shown as pieces of the pie. The function adds up all the x values to compare part and whole and auto-generate the pieces of the pie.

labels: the variable used to label each section of the pie chart.

startangle: the rotation of the pie chart, adjusted to improve readability.

colors: an array of colors the chart will cycle through. If blank, defaults to matplotlib’s default 10-color “Tableau” palette.

## Historgram chart

```
plt.hist(x = df.shoe_size, bins = 12, range = (5, 12), color = 'dodgerblue')
```
x: the value being distributed (like shoe size, or height) – note that it should not be an aggregated value.

bins: specifies how many bins to make (e.g. 10) OR where the edges of the bins are (as a list of values).

range: the lower and upper range of the bins. If unspecified, set to the min and max values for x.

color: sets the color of the bars.  

## AB line

```
plt.bar( x = school_subject, y = test_score)
plt.axhline(y = 85, xmin = 0, xmax = 1, linewidth = 2, color = red)
```

x: where to position the line along the x-axis.

ymin: how close to the bottom of the graph the line starts. Setting ymin=0 starts the line at the bottom of the graph, ymin=.5 would start it halfway up, and ymin=1 would start at the top of the graph. Usually set to 0.

ymax: how close to the bottom of the graph the line ends. Setting ymax=0 ends the line at the bottom of the graph, ymax=.5 would end it halfway up, and ymax=1 would end at the top of the graph. Usually set to 1.

linewidth: line width of the AB line.

dashes: dash pattern given as (line_length, space_length).

color: color of the AB line.

plt.annotate() takes the following arguments:

text: annotation text.

xy: (x, y) coordinate position for annotation.

color: color of annotation text and arrow.
