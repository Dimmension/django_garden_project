-- migrate:up

create extension if not exists "uuid-ossp";

create schema if not exists garden;

set search_path to public, garden;

drop table if exists 
garden.coord, 
garden.taxon,
garden.collect_place,
garden.label,
garden.herbarium,
garden.comment,
garden.flora 
cascade;

create table garden.coord(
id				uuid primary key default uuid_generate_v4(), 
altitude        decimal,
longitude       decimal,
latitude        decimal,
geog_point      GEOGRAPHY(Point)
);

create table garden.taxon (
id 				uuid primary key default uuid_generate_v4(), 
domain 			text,
kingdom 		text,
phylum 			text, 
klass 			text,
ordo 			text,
family			text,
genus 			text not null,
species	 		text not null,
subspecies 		text
);

create table garden.collect_place (
id uuid primary key default uuid_generate_v4(), 
country 		text,
region			text,
city			text,
coord_id        uuid references garden.coord unique
);

create table garden.herbarium (
id				uuid primary key default uuid_generate_v4(), 
depart 			text,
region			text
);

create table garden.comment (
id				uuid primary key default uuid_generate_v4(), 
description 	text,
cool_facts		text,
ww_distribution	text,
protect			text
);

create table garden.flora (
id 					uuid primary key default uuid_generate_v4(), 
alive 				boolean,
author 				text,
geo_author		    text,
rus_name 			text,
taxonomycol			text,
autochthony 		text,
picture             text,
taxon_id 			uuid references garden.taxon unique,
collect_place_id	uuid references garden.collect_place unique,
herbarium_id 		uuid references garden.herbarium unique,
comment_id			uuid references garden.comment unique,
created 			timestamp with time zone default CURRENT_TIMESTAMP
);

create table garden.label (
id				uuid primary key default uuid_generate_v4(), 
institute 		text,
project 		text,
name 			text,
description 	text,
morph_features 	text,
collected 		date,
plant_id 		uuid references garden.flora,
coord_id 		uuid references garden.coord unique
);

-- migrate:down