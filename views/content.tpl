<div class="container-fluid">
% if current_row:
<h1>
{{current_row[0]}}
</h1>

<form>

% for i, column_name in enumerate(current_resource["data"]["columns"]):
    <label for="input{{i}}" class="form-label">{{column_name}}</label>
    <input class="form-control" id="input{{i}}" value={{current_row[i]}}>
% end
<button type="submit" class="btn btn-primary">Сохранить</button>

</form>

% elif current_resource:
    <h1>{{current_resource["title"]}}</h1>

      <table class="table">
      <thead>
            <tr>
                % for column_name in current_resource["data"]["columns"]:
                    <th>{{column_name}}</th>
                % end
            </tr>
          </thead>
          <tbody>

          % for row in current_resource["data"]["data"]:
                <tr onclick="document.location = `${document.location}/{{row[0]}}`;">
                % for col in row:
                    <th>
                        {{col}}
                    </th>
                % end
                </tr>
          % end
        </tbody>
    </table>
% end
</div>