class UniqueNameMixin:
    
    def clean(self):
        super().clean()
        self.name = self.name.upper()
        
class DropdownMixin:
    template_name = "location/dropdown_list_options.html"
