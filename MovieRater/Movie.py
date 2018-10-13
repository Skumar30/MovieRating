class Movie(dict):
    name = ''
    imdbRating = -1
    boxOffice = -1
    meta = -1
    rogerRating = -1
    googleRating = -1
    genreTags = []
    starCast = []
    releaseYr = -1

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)
