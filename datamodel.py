from google.appengine.ext import db
from google.appengine.ext import blobstore

class Offers(db.Model):
  store=db.StringProperty()
  title=db.StringProperty()
  offer_position=db.StringProperty(default="Main",choices=set(["Main", "Widget","Top","Popular","DayDeal","iframe","Others"]))
  offer_type= db.StringProperty(choices=set(["Coupon", "Deal"]))
  coupon_code = db.StringProperty(default="NO CODE")
  aff_link=db.LinkProperty()
  description=db.TextProperty()
  expiry=db.DateProperty()
  posted_on = db.DateTimeProperty(auto_now_add=True)
  category=db.StringProperty()
  sub_category=db.StringProperty()
  ideal_for= db.StringProperty()
  effid_1 =db.IntegerProperty(default=0)
  effid_2=db.IntegerProperty(default=0)
  likes=db.IntegerProperty(default=0)
  dislike=db.IntegerProperty(default=0)
  editors_pick=db.BooleanProperty(default=False)
  clicks = db.IntegerProperty(default=0)
  blob_key = blobstore.BlobReferenceProperty()
  enabled=db.BooleanProperty(default=True)
  def to_dict(self):
       return dict([(p, unicode(getattr(self, p))) for p in self.properties()])


class Users(db.Model):
  user = db.UserProperty()
  user_type =db.StringProperty(default='Regular',choices=set(["Admin","Support","Developer", "Regular", "General"]))
  name= db.StringProperty()
  email =db.EmailProperty(required=True)
  gender = db.StringProperty(default='Select',choices=set(["Select", "Male", "Female"]))
  clicks = db.IntegerProperty(default=0)
  visit_count=db.IntegerProperty(default=1)
  subscribed = db.BooleanProperty(default=False)
  
class Stores(db.Model):
  store = db.StringProperty()
  affid = db.StringProperty()
  tagname =  db.StringProperty()
  store_link = db.LinkProperty()
  coupons_count = db.IntegerProperty(default=0)
  deals_count = db.IntegerProperty(default=0)
  # blob_key=db.StringProperty()
  blob_key = blobstore.BlobReferenceProperty()