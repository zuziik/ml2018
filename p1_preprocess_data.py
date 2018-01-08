## Preprocesses data from the original data files into one merged dataset

import numpy as np
from movie_lengths_lib import *

#------------------------------------------------------------------------------

def get_data_from_files ( file_title, file_crew, file_name ):
    data = {}
    director_ids = set()
    genres = set()
    types = set()
    director_years = {}
    no = "\\N"
    
    with open ( file_title, 'r' ) as f:
        next (f)
        for line in f:
            attr = line[:-1].split ('\t')
            if (attr[1] == no) or (attr[4] == no) or (attr[5] == no) or (attr[7] == no) or (attr[8] == no):
                continue
            movie = {}
            movie_id = int (attr[0][2:])
            movie ['type'] = attr[1]
            movie ['adult'] = bool (attr[4])
            movie ['year'] = int (attr[5])
            movie ['length'] = int (attr[7])
            movie ['genres'] = attr[8].split(',')
            
            for genre in movie ['genres']:
                if genre not in genres:
                    genres.add (genre)
                    
            if movie ['type'] not in types:
                types.add (movie ['type'])
                
            data [movie_id] = movie
            
    print ( "--- {}".format(file_title) )

    with open ( file_crew, 'r' ) as f:
        next (f)
        for line in f:
            attr = line[:-1].split ('\t')
            movie_id = int (attr[0][2:])
            if (movie_id in data) and (attr[1] != no) and (len(attr[1].split(',')) == 1):
                movie = data [movie_id]
                movie ['director_id'] = attr[1]
                data [movie_id] = movie
                if attr[1] not in director_ids:
                    director_ids.add (attr[1])
                
    print ( "--- {}".format(file_crew) )

    with open ( file_name, 'r' ) as f:
        next (f)
        for line in f:
            attr = line[:-1].split ('\t')
            if (attr[0] in director_ids) and (attr[2] != no):
                director_years [attr[0]] = int (attr[2])
                
    print ( "--- {}".format(file_name) )

    # Clear data and return as a numpy array
    matrix = []
    genres_ordered = list (genres)
    types_ordered = list (types)
    
    for movie in data.values():
        if ('director_id' in movie) and (movie['director_id'] in director_years):
            line = [ movie ['adult'], movie ['year'], director_years [movie['director_id']]]
            for genre in genres_ordered:
                if genre in movie ['genres']:
                    line.append (1)
                else:
                    line.append (0)
            for m_type in types_ordered:
                if m_type == movie ['type']:
                    line.append (1)
                else:
                    line.append (0)
            line.append (movie['length'])
            matrix.append (line)
    
    header = ['adult', 'movie_year', 'director_year'] + genres_ordered + types_ordered

    return np.matrix (matrix), np.matrix (header)

#------------------------------------------------------------------------------

print ( "Starting data loading..." )
data, header = get_data_from_files ( file_title, file_crew, file_name )
print ( "Loaded data from files, {} lines".format(len(data)) )
print ()

print ( "Saving data to files" )

for (d, fn) in [(data, file_data), (header, file_header)]:
    dump_data_to_file ( d, fn )
    print ( "--- {}".format(fn) )