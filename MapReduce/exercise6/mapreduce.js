///
/// MapReduce for Categry Counts
///
map = function(){
            emit(this.category, 1);
};

reduce = function reduce(key, values) {
  return values.length;
};

res = db.reoticos.mapReduce(map, reduce, {out: 'categories_count'});



// MapReduce for Month Counts

map_count_by_months = function(){
    var date = new Date(this.date);
    var month = date.getMonth()+1;
    emit({month: month }, {count: 1});
}

// marqueze
ma_reduce_count = function(key, values) {
    var total = 0;
    for (var i = 0; i < values.length; i++) {
        total += values[i].count;
    }
    return { count : total, relative: ((total / 25873) * 100).toFixed(3) };
}

// relatos_eroticos
re_reduce_count = function(key, values) {
    var total = 0;
    for (var i = 0; i < values.length; i++) {
        total += values[i].count;
    }
    return { count : total, relative: ((total / 4079) * 100).toFixed(3) };
}


res = db.marqueze.mapReduce(map_count_by_months, ma_reduce_count, {out: 'ma_count_by_months'});
res = db.reoticos.mapReduce(map_count_by_months, re_reduce_count, {out: 're_count_by_months'});

// MapReduce for Year Counts

map_count_by_year = function(){
    var date = new Date(this.date);
    var year = date.getFullYear();
    emit({year: year }, {count: 1});
}

res = db.reoticos.mapReduce(map_count_by_year, re_reduce_count, {out: 're_count_by_year'});
res = db.marqueze.mapReduce(map_count_by_year, ma_reduce_count, {out: 'ma_count_by_year'});
