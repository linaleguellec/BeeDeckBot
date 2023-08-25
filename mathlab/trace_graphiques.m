% Charger les fichiers .mat
fileNames = {'X.mat', 'Y.mat', 'Z.mat'};
dataFields = cell(1, numel(fileNames));

for i = 1:numel(fileNames)
    fileName = fileNames{i};
    loadedData = load(fileName);
    fields = fieldnames(loadedData); % Trouver les noms des champs dans le fichier
    % Remplacez 'nom_du_champ' par le nom réel du champ que vous voulez utiliser
    dataFields{i} = fields{1}; % Supposons que le champ souhaité soit le premier champ
end

% Vérification de la taille des données (assumer que les tailles sont identiques)
dataSize = size(data{1});
for i = 2:numel(data)
    if ~isequal(size(data{i}), dataSize)
        error('Les tailles des données ne correspondent pas.');
    end
end

% Créer un maillage de coordonnées pour le tracé en 3D
[x, y, z] = meshgrid(1:dataSize(2), 1:dataSize(1), 1:numel(data));

% Créer la figure 3D
figure;
scatter3(x(:), y(:), z(:), 50, data{1}(:), 'filled');
hold on;
scatter3(x(:), y(:), z(:), 50, data{2}(:), 'filled');
scatter3(x(:), y(:), z(:), 50, data{3}(:), 'filled');
colorbar;

xlabel('Axe X');
ylabel('Axe Y');
zlabel('Fichiers');

title('Graphique en 3D à partir des fichiers .mat');
legend('X', 'Y', 'Z');

grid on;
hold off;
