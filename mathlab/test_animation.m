% Exemple de données 3D (remplacez-les par vos propres données)
t = linspace(0, 2*pi, 100);  % Créez des valeurs pour le temps
x = sin(t);                 % Coordonnées X
y = cos(t);                 % Coordonnées Y
z = t;                      % Coordonnées Z

% Chargez votre image PNG (remplacez 'votre_image.png' par le nom de votre image)
image = imread('fleur.png');

% Créez une nouvelle figure
figure;


% Créez un objet VideoWriter en spécifiant la résolution souhaitée
outputVideo = VideoWriter('animation_3D_with_image.mp4', 'MPEG-4');
% outputVideo.FrameRate = 30;  % Réglage facultatif : spécifiez le taux de trame souhaité
% outputVideo.Quality = 100;   % Réglage facultatif : spécifiez la qualité vidéo
% 
% % Définissez la résolution de la vidéo (largeur x hauteur)
% outputVideo.Width = 1280;   % Largeur souhaitée
% outputVideo.Height = 720;   % Hauteur souhaitée

open(outputVideo);

% Boucle pour créer l'animation
for i = 1:length(t)
    % Effacez la figure précédente
    clf;
    
    % Tracer le graphique 3D actuel
    plot3(x(1:i), y(1:i), z(1:i), 'b-');
    
    % Personnalisez le graphique (titre, étiquettes d'axe, etc.)
    title('Animation 3D avec Image');
    xlabel('Axe X');
    ylabel('Axe Y');
    zlabel('Axe Z');
    
    % Limitez les axes X, Y et Z si nécessaire (ajustez les limites selon vos besoins)
    axis([-1 1 -1 1 0 2*pi]);
    
    % Affichez la grille
    grid on;
    
    % Affichez l'image PNG sur le plan XY (ajustez les coordonnées XY en fonction de l'emplacement souhaité)
    % La fonction 'imshow' prend en charge l'affichage d'images PNG
    imshow(image, 'XData', [-0.001 0.001], 'YData', [-0.001 0.001]);
    
    % Mettez en pause pour contrôler la vitesse de l'animation (ajustez la valeur en fonction de la vitesse souhaitée)
    pause(0.05);
    
    % Capturez la figure pour enregistrer l'animation
    frame = getframe(gcf);
    
    % Écrivez le frame dans la vidéo
    writeVideo(outputVideo, frame);
end

% Fermez la vidéo
close(outputVideo);
