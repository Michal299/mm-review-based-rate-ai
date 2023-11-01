# API Discovery

## Movies search
**Movies list**\
Request: `/api/v1/films/search`\
Pagins? Yes, for example `/api/v1/films/search?page=2`\
Example: 
```json
{
	"total": 10000,
	"searchHits": [
		{
			"id": 862,
			"type": "film",
			"filmMainCast": [
				{
					"id": 124,
					"name": "Tom Hanks"
				},
				{
					"id": 3454,
					"name": "David Morse"
				}
			]
		},
		{
			"id": 1048,
			"type": "film",
			"filmMainCast": [
				{
					"id": 90,
					"name": "Tim Robbins"
				},
				{
					"id": 176,
					"name": "Morgan Freeman"
				}
			]
		},
        ...
	]
}
```
**Get ratings for movie**\
Request: `/api/v1/film/<movie_id>/rating`\
Example `/api/v1/film/1262/rating`:
```json
{
	"count": 311491,
	"rate": 7.81072,
	"countWantToSee": 83560,
	"countVote1": 1355,
	"countVote2": 1008,
	"countVote3": 2676,
	"countVote4": 4748,
	"countVote5": 10846,
	"countVote6": 25157,
	"countVote7": 64132,
	"countVote8": 103233,
	"countVote9": 60741,
	"countVote10": 37595
}
```

## Movie data
### Reviews
**Get critics for movie**\
Request:`/api/v1/film/<movie_id>/critics`\
Example: `/api/v1/film/10036496/critics`\
```json
[
	867323
]
```
**Get all critics**\
Request: `/api/v1/film/critics`\
Example: 
```json
[
	{
		"id": 1164541,
		"userName": "michaloleszczyk",
		"priority": 1,
		"publisher": "Spoiler Master Podcast"
	},
	{
		"id": 1243927,
		"userName": "tru3",
		"priority": 1,
		"publisher": "Magazyn SFP"
	},
    ...
]
```

**Get review**\
Request: `/api/v1/user/<critic_name>/vote/film/<movie_id>`\
Example for `/api/v1/user/dem3000/vote/film/297829`: 
```json
{
	"rate": 6,
	"user": 2595124,
	"comment": "Często liryczny obrazem i słowem w stylu cytatów wrzucanych przez mamy na Facebooku. Śliczne zdjęcia i sama historia ma w sobie sporo mocy.",
	"viewDate": 20150215,
	"likes": [
		1674467,
		2937305,
		1442210,
		2159391,
		1269555,
		1885093,
		2010239,
		2172106,
		2451245,
		1699183,
		1847690,
		1511169,
		2536487,
		640604,
		1547404,
		2669376,
		2604848,
		2062304,
		1480058
	],
	"timestamp": 1424038589438
}
```