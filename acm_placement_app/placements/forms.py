from django import forms

from acm_placement_app.placements.models import PlacementRequest
from acm_placement_app.placements.utils import get_acm_survey_missing_columns

RUN_PARAMS_FIELDS = [
    'num_iterations',
    'prevent_roommates',
    'consider_HS_elig',
    'calc_commutes',
    'commute_date',
    'commutes_reference_file',
]

FACTOR_IMPORTANCE_FIELDS = [
    'commute_factor',
    'ethnicity_factor',
    'gender_factor',
    'edscore_factor',
    'spanish_factor',
]

BLANK_COLS_WARNING_MSG = """Warning: the following columns could not be resolved from your survey file. 
These columns will be filled with blanks if you choose to continue:"""


class PlacementRequestSchoolDataForm(forms.ModelForm):
    class Meta:
        model = PlacementRequest
        fields = [
            'school_data_file'
        ]


class PlacementRequestACMSurveyDataForm(forms.ModelForm):

    def get_warnings(self):
        warnings = {}
        _, missing_columns = get_acm_survey_missing_columns(self.files['acm_survey_data_form-acm_survey_data_file'])
        if missing_columns:
            warnings['message'] = BLANK_COLS_WARNING_MSG
            warnings['list'] = missing_columns
        return warnings

    class Meta:
        model = PlacementRequest
        fields = [
            'acm_survey_data_file'
        ]


class PlacementRequestRunParametersForm(forms.ModelForm):
    class Meta:
        model = PlacementRequest
        fields = RUN_PARAMS_FIELDS


class PlacementRequestFactorImportanceForm(forms.ModelForm):
    class Meta:
        model = PlacementRequest
        fields = FACTOR_IMPORTANCE_FIELDS


def get_placementrequest_instance_from_form_list(form_list, commit=True):
    school_data_form, acm_survey_data_form, run_parameters_form, factor_importance_form = form_list
    placementrequest = run_parameters_form.save(commit=False)

    # Uploaded files
    placementrequest.school_data_file = school_data_form.instance.school_data_file
    placementrequest.acm_survey_data_file = acm_survey_data_form.instance.acm_survey_data_file

    # Factor importances
    if factor_importance_form.is_valid():
        for field_name in FACTOR_IMPORTANCE_FIELDS:
            setattr(placementrequest, field_name, factor_importance_form.cleaned_data[field_name])

    if run_parameters_form.is_valid():
        if run_parameters_form.cleaned_data['commutes_reference_file']:
            placementrequest.commute_factor = 0

    if commit:
        placementrequest.save()
    return placementrequest
