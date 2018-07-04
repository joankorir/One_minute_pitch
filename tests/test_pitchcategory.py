from app.models import PitchCategory
from app import db

def setUp(self):
   self.new_category = PitchCategory(id=345,name = Interview , description = Finerr)


def tearDown(self):
    PitchCategory.query.delete()


def_test_check_instance_variables(self):
     self.assertEquals(self.new_category.id,345)
     self.assertEquals(self.new_category.name,Interview)
     self.assertEquals(self.new_category.description,Finerr)

def_save_review(self):
  self.new_category.save_category()
  self.assertEquals(len(PitchCategory.query.all())>0)

def test_get_categories_by_id(self):

    self.new_category.save_category()
    got_categories = PitchCategory(345)
    self.assertTrue(len(got_categories) ==1 )
