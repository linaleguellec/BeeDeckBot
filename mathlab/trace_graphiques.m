%% 
load('trajectoire2.mat'); % Chargez le fichier .mat

Xmm = trajectoire2.Xmm
Ymm = trajectoire2.Ymm
Zmm = trajectoire2.Zmm

% Tracer le graphique en 3D
figure; % Créez une nouvelle figure
plot3(Xmm, Ymm, Zmm, 'r-', 'LineWidth', 2); 
xlabel('Axe X'); % Étiquette de l'axe X
ylabel('Axe Y'); % Étiquette de l'axe Y
zlabel('Axe Z'); % Étiquette de l'axe Z
title('Graphique en 3D'); % Titre du graphique

% Limitez les axes X, Y et Z si nécessaire (ajustez les limites selon vos besoins)
axis([0 550 0 450 0 463]);

% Personnalisez le graphique selon vos besoins
grid on; % Affiche une grille


hold on 

% Tracé du cube  
plot3([0, 550], [0, 0], [0, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
plot3([0, 0], [0, 450], [0, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
plot3([0, 0], [0, 0], [0, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire

plot3([550, 550], [450, 450], [463, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
plot3([550, 0], [450, 450], [463, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
plot3([550, 550], [450, 0], [463, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire


plot3([550, 550], [0, 0], [463, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
plot3([550, 550], [0, 450], [0, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
plot3([550, 0], [450, 450], [0, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
plot3([0, 0], [450, 450], [0, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire

plot3([0, 0], [450, 0], [463, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
plot3([0, 550], [0, 0], [463, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire

% tracé de la porte
plot3([550, 550], [50, 100], [400, 400], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
plot3([550, 550], [50, 50], [400, 450], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
plot3([550, 550], [100, 100], [450, 400], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
plot3([550, 550], [100, 50], [450, 450], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire

% tracé de la fleur

hold on 

% Exemple de données (remplacez-les par vos propres données)
t = linspace(0, 2*pi, 100);  % Créez des valeurs pour l'angle t
r = 50;  % Rayon du cercle
r1 = 37.5
r2 = 25

x0 = 285
y0 = 87
% Calcul des coordonnées du cercle dans l'espace 3D
x = x0 + r * cos(t);  % Coordonnées X du cercle
y = y0 + r * sin(t);  % Coordonnées Y du cercle

z = 36*ones(size(t));  % Coordonnées Z du cercle (tous les z sont à zéro)

x1 = x0 + r1 * cos(t);  % Coordonnées X du cercle
y1 = y0 + r1 * sin(t);  % Coordonnées Y du cercle

x2 = x0 + r2 * cos(t);  % Coordonnées X du cercle
y2 = y0 + r2 * sin(t);  % Coordonnées Y du cercle

% Tracer le graphique 3D avec le cercle rempli en bleu
fill3(x, y, z, 'g');  % Utilisez 'b' pour remplir le cercle en bleu
fill3(x1, y1, z, 'b');  % Utilisez 'b' pour remplir le cercle en bleu
fill3(x2, y2, z, 'g');  % Utilisez 'b' pour remplir le cercle en bleu

hold off

view(3); % Affiche la vue en 3D

%%




% partie animation
% Créez une nouvelle figure
figure;

% Créez un objet VideoWriter pour enregistrer la vidéo au format MP4
outputVideo = VideoWriter('animation_3D.mp4', 'MPEG-4');
open(outputVideo);



% Boucle pour créer l'animation
for i = 1:length(Xmm)
    % Effacez la figure précédente
    clf;
    
    % Tracer le graphique 3D actuel
    plot3(Xmm(1:i), Ymm(1:i), Zmm(1:i), 'r-', 'LineWidth', 2);
    
    % Personnalisez le graphique (titre, étiquettes d'axe, etc.)
    title('Animation 3D');
    xlabel('Axe X');
    ylabel('Axe Y');
    zlabel('Axe Z');
    
    % Limitez les axes X, Y et Z si nécessaire (ajustez les limites selon vos besoins)
    axis([0 550 0 450 0 463]);
  
    % Affichez la grille
    grid on;
    
    hold on 
    
    % Tracé du cube  
    plot3([0, 550], [0, 0], [0, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
    plot3([0, 0], [0, 450], [0, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
    plot3([0, 0], [0, 0], [0, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire

    plot3([550, 550], [450, 450], [463, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
    plot3([550, 0], [450, 450], [463, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
    plot3([550, 550], [450, 0], [463, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire


    plot3([550, 550], [0, 0], [463, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
    plot3([550, 550], [0, 450], [0, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
    plot3([550, 0], [450, 450], [0, 0], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
    plot3([0, 0], [450, 450], [0, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire

    plot3([0, 0], [450, 0], [463, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
    plot3([0, 550], [0, 0], [463, 463], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire

    % tracé de la porte
    plot3([550, 550], [50, 100], [400, 400], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
    plot3([550, 550], [50, 50], [400, 450], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
    plot3([550, 550], [100, 100], [450, 400], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire
    plot3([550, 550], [100, 50], [450, 450], 'k', 'LineWidth', 2);  % 'k' spécifie la couleur noire

    % tracé de la fleur

    hold on 

    % Exemple de données (remplacez-les par vos propres données)
    t = linspace(0, 2*pi, 100);  % Créez des valeurs pour l'angle t
    r = 50;  % Rayon du cercle
    r1 = 37.5
    r2 = 25

    x0 = 285
    y0 = 87
    % Calcul des coordonnées du cercle dans l'espace 3D
    x = x0 + r * cos(t);  % Coordonnées X du cercle
    y = y0 + r * sin(t);  % Coordonnées Y du cercle

    z = 36*ones(size(t));  % Coordonnées Z du cercle (tous les z sont à zéro)

    x1 = x0 + r1 * cos(t);  % Coordonnées X du cercle
    y1 = y0 + r1 * sin(t);  % Coordonnées Y du cercle

    x2 = x0 + r2 * cos(t);  % Coordonnées X du cercle
    y2 = y0 + r2 * sin(t);  % Coordonnées Y du cercle

    % Tracer le graphique 3D avec le cercle rempli en bleu
    fill3(x, y, z, 'g');  % Utilisez 'b' pour remplir le cercle en bleu
    fill3(x1, y1, z, 'b');  % Utilisez 'b' pour remplir le cercle en bleu
    fill3(x2, y2, z, 'g');  % Utilisez 'b' pour remplir le cercle en bleu

    
    % Mettez en pause pour contrôler la vitesse de l'animation (ajustez la valeur en fonction de la vitesse souhaitée)
    pause(0.02);
    
    % Capturez la figure pour enregistrer l'animation
    frame = getframe(gcf);
    
    % Écrivez le frame dans la vidéo
    writeVideo(outputVideo, frame);
end

% Fermez la vidéo
close(outputVideo);








