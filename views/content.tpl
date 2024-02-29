<div class="container-fluid">
% if current_resource:
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
            <tr>
                % for row in current_resource["data"]["data"]:
                    % for col in row:
                        <th>{{col}}</th>
                    % end
                % end
            </tr>
        </tbody>
    </table>
% end
</div>