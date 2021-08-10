Making Space
===
We want to have some space for our tank and the enemy tanks. Our tank is at the bottom, and the enemy tanks are going to be at the top. So let's leave the top and bottom rows empty.

### Exclude bottom row
To exclude the bottom row, we just need to reduce the number of rows drawn by one. Previously, we drew 12 rows using...

```for y in range(12):```

...so let's change it to 11 rows...

```for y in range(11):```

That leaves the bottom row empty.

### Exclude top row
To exclude the top row (...to make space for the enemies), we need to exclude another row. So...

```for y in range(10):```

...but that will leave two rows empty at the bottom! To shift it all down, we'll add another 50 to the **y** position of the walls.

```wall.y = y * 50 + 25 + 50```

Now both the top and bottom rows are empty!