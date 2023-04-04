import pandas as pd

animals = pd.DataFrame(
    {
        'species': ['Lion', 'Giraffe', 'Elephant'],
        'Africa': [5,12,8],
        'Asia': [0,1,2],
    }
)

# reformat for 1 row for continent and species combination
melted_animals = animals.melt(
        id_vars='species',
        value_vars=['Africa', 'Asia'],
        var_name='continent',
        value_name='population',
)

pivoted_animals = melted_animals.pivot(index='species',
                     columns='continent',
                     values='population')
pivoted_animals.index.name = None
pivoted_animals

