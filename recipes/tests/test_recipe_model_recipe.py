from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeModelTest(RecipeTestBase):

    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_if_title_has_more_65_chars(self):
        self.recipe.title = ''.rjust(70, 'A')

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
