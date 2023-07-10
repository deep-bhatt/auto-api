from fastapi import APIRouter, Request
from autoapi.services import common
from itertools import groupby

router = APIRouter()


@router.get('/data/', tags=['Fetch data'])
def get_data(request: Request):
    valid_fields = []
    requested_fields = []
    conditions = {}

    valid_field_results = common.query_all_field_names()
    for row in valid_field_results:
        valid_fields.append(row['field_name'])

    # indicates which fields to fetch
    for key, val in request.query_params.items():
        if key == 'fields':
            requested_fields = val.split(',')
            for i in range(len(requested_fields)):
                requested_fields[i] = requested_fields[i].strip()
        elif key == 'limit' or key == 'offset':
            pass
        else:
            if key in valid_fields:
                conditions[key] = val

    if not conditions:
        return []

    results = common.build_and_run_api(conditions)
    sorted_data = sorted(results, key=lambda x:x['row_id'])
    grouped_data = groupby(sorted_data, key=lambda x: x['row_id'])

    rows_id_to_consider = []
    for row_id, group in grouped_data:
        group_list = list(group)

        if len(group_list) < len(conditions):
            continue

        # print(f"row_id: {row_id}")
        should_consider_row = True
        for item in group_list:
            if item['field_name'] not in conditions or item['field_value'] != conditions[item['field_name']]:
                should_consider_row = False
        if should_consider_row:
            rows_id_to_consider.append(row_id)

    results = common.fetch_dataset_rows(tuple(rows_id_to_consider))
    grouped_data = groupby(results, key=lambda x: x['row_id'])

    return_list = []
    for row_id, group in grouped_data:
        t_dict = {}
        for row in group:
            if not requested_fields or len(requested_fields) == 0:
                t_dict[row['field_name']] = row['field_value']
            elif row['field_name'] in requested_fields:
                t_dict[row['field_name']] = row['field_value']
        return_list.append(t_dict)

    return {'results': return_list}
