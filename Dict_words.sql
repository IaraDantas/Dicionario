--drop table palavras
--drop table words
create table palavras (
    id integer primary key,
    palavra text not null unique,
    traducao text not null,
    contador_acesso integer not null
);


create table words (
    id integer primary key,
    palavra text not null unique,
    traducao text not null,
    contador_acesso integer not null
);

select * from palavras;
select * from words;

select palavra, contador_acesso from palavras union all select palavra, contador_acesso from words order by contador_acesso desc limit 10
