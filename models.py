class Post:
    def __init__(self, post, category = None, score = None, active = None):
        self.post = post
        self.category = category
        self.score = score
        self.active = active