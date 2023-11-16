# movies_home
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
# Let us import the app object in case we need to define
# callbacks here
from app import app
#for DB needs
from apps import dbconnect as db
from apps.movies import movies_profile

# store the layout objects into a variable named layout
layout = html.Div(
    [
        html.H2('Movies'), # Page Header
        html.Hr(),
        dbc.Card( # Card Container
            [
                dbc.CardHeader( # Define Card Header
                    [
                        html.H3('Manage Records')
                    ]
                ),
                dbc.CardBody( # Define Card Contents
                [   
                        html.Div( # Add Movie Btn
                            [
                                # Add movie button will work like a
                                # hyperlink that leads to another page
                                dbc.Button('Add Movie', color="secondary", href='/movies/movies_profile?mode=add'),
                            ]
                        ),
                        html.Hr(),
                        html.Div( # Create section to show list of movies
                            [
                                html.H4('Find Movies'),
                                html.Div(
                                    dbc.Form(
                                        dbc.Row(
                                            [
                                                dbc.Label("Search Title", width=1),
                                                dbc.Col(
                                                    dbc.Input(
                                                        type='text',
                                                        id='moviehome_titlefilter',
                                                        placeholder='Movie Title'
                                                    ),
                                                    width=5
                                                )
                                            ],
                                            className = 'mb-3'
                                        )
                                    )
                                ),
                                html.Div(
                                    id='moviehome_movielist'
                                )
                            ]
                        )   
                    ]
                )
            ]   
        )
    ]
)

@app.callback(
[
    Output('moviehome_movielist', 'children')
],
[
    Input('url', 'pathname'),
    Input('moviehome_titlefilter', 'value'), # changing the text box value should update the table
]
)
def moviehome_loadmovielist(pathname, searchterm):
    if pathname == '/movies':
    # 1. Obtain records from the DB via SQL
    # 2. Create the html element to return to the Div
        sql = """ SELECT movie_name, genre_name, movie_id
        FROM movies m
        INNER JOIN genres g ON m.genre_id = g.genre_id
        WHERE
        NOT movie_delete_ind
        """
        values = [] # blank since I do not have placeholders in my SQL
        cols = ['Movie Title', 'Genre', 'ID']
        ### ADD THIS IF BLOCK
        if searchterm:
        # We use the operator ILIKE for pattern-matching
            sql += " AND movie_name ILIKE %s"
        # The % before and after the term means that
        # there can be text before and after
        # the search term
            values += [f"%{searchterm}%"]
        df = db.querydatafromdatabase(sql, values, cols)
        if df.shape: # check if query returned anything

            buttons = []
            for movie_id in df['ID']:
                buttons +=  [
                    html.Div(
                        dbc.Button('Edit',href=f'movies/movies_profile?mode=edit&id={movie_id}',
                                   size='sm', color='warning'),
                                   style={'text-align': 'center'}
                    )
                ]
            df['Action'] =buttons
            df= df[['Movie Title', 'Genre', "Action"]]

            table = dbc.Table.from_dataframe(df, striped=True, bordered=True,
            hover=True, size='sm')
            return [table]
        else:
            return ["No records to display"]
    else:
        raise PreventUpdate
