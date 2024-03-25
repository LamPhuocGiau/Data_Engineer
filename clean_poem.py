highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)

highlighted_poems_stripped =[]
for x in highlighted_poems_list:
  highlighted_poems_stripped.append(x.strip())
print(highlighted_poems_stripped)

highlighted_poems_details = []
for y in highlighted_poems_stripped:
  highlighted_poems_details.append(y.split(":"))
  print(highlighted_poems_details)

titles = []
poets = []
dates = []
for temp in highlighted_poems_details:
    titles.append(temp[0])
    poets.append(temp[1])
    dates.append(temp[2])
print(titles)
print(poets)
print(dates)

for idx in range(len(dates)):
  print("The poem {titles} was published by {poets} in {dates}.".format(titles = titles[idx], poets = poets[idx], dates = dates[idx]))




