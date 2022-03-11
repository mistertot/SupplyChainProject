### ===========================================================================
### Graphiques des KPI produits par le checker. Ne pas hésiter à ajouter ses
### propres graphiques selon ses besoins. Voir les exemples proposés.
### ===========================================================================

#INSTANCE <- "mini"    # choix de l'instance (NULL pour utilisation de CONFIG)
INSTANCE <- NULL      # instance déterminée par CONFIG
PDF <- FALSE          # graphiques produits dans un PDF {instance}.pdf ?
LOG <- TRUE           # Outputs log file (all messages from checker)

### ===========================================================================
### Lecture des données. Ne modifiez cette partie qu'à vos risques et périls !

## Lecture de la configuration
if (is.null(INSTANCE)){
  if (!file.exists("CONFIG")) stop("ERREUR : Ni instance ni fichier CONFIG fournis (arrêt).", call. = F)
  INSTANCE <- grep("^INSTANCE *=", readLines("CONFIG"), value = TRUE)
  if (length(INSTANCE) == 0) stop("ERREUR : Aucun instance indiquée dans CONFIG (arrêt).", call. = F)
  INSTANCE=strsplit(INSTANCE, " *= *")[[1]][2]
}

if (LOG){
  LOG <- sprintf("%s.log", INSTANCE)
  if (!file.exists(LOG)) stop(sprintf("ERREUR : Le fichier de message %s n'existe pas (arrêt)", LOG), call. = F)
  cat(readLines(LOG), sep="\n")
}

KPI <- sprintf("%s.kpi", INSTANCE)
if (!file.exists(KPI)) stop(sprintf("ERREUR : Le fichier d'indicateur %s n'existe pas (arrêt)", KPI), call. = F)
message(sprintf("Graphes pour l'instance : %s", INSTANCE))


## Lecture de tous les indicateurs
kpi <- read.delim(KPI, sep=";", dec=".")

## La première ligne contient en fait les valeurs de références (capacités ou 
## coûts unitaires) ; elle est transférée dans une autre base de données.
references <- kpi[1,]
kpi <- kpi[-1,]

### ===========================================================================
### Fonctions auxiliaires bien pratiques !

## Renvoie les noms de colonnes correspondant aux critères d'inclusion/exclusion indiqués.
## - inclure et exclure sont des vecteurs de chaînes de caractères ; on est inclut ou exclut
## si l'une de ces chaînes apparaît dans le nom de la colonne.
## - ^ et $ indiquent respectivement le début et la fin du nom
## exemples :
## - selection("stock") : toutes les colonnes qui contiennent "stock"
## - selection("stock$") : toutes les colonnes dont le nom termine par stock
## - selection(c("stock", "prod"), exclure="cout") : toutes les colonnes avec "stock" ou "prod", sauf celles avec "cout"
selection <- function(inclure=NULL, exclure=NULL){
  if (is.null(inclure)){
    sel <- names(kpi)
  }else{
    sel <- c()
    for(p in inclure) sel <- c(sel, grep(p, names(kpi), value=T))
    sel <- unique(sel)
  }
  
  if (!is.null(exclure)){
    for(p in exclure) 
      sel <- grep(p, sel, value=T, invert=T)
  }
  return(sort(sel))
}

### Trace l'évolution des colonnes sélectionnées.
### - sel  : (vecteur) des noms des colonnes à afficher
### - ylab : nom de l'axe des ordonnées
### - ylim (optionnel) : échelle des ordonnées
### - ref  (optionnel) : si les valeurs de références sont tracées ou pas
evolution <- function(sel, nom, ylim=NULL, ref=FALSE){
  if (is.null(ylim)) ylim = c(0, max(kpi[, sel]))
  plot(NA, 
       xlim=range(kpi$jour),  xlab="",
       ylim=ylim, ylab="")
  mtext(text = "jour", side = 1, line = 2, cex=0.8)
  mtext(text = nom, side = 2, line = 2, cex=0.8)
  for(i in 1:length(sel)){
    if (sprintf("%s_ect", sel[i]) %in% names(kpi)){
      ect <- kpi[, sprintf("%s_ect", sel[i])]
      lines(kpi$jour, kpi[, sel[i]] - ect, col=i+1, lwd=3, lty=2)
      lines(kpi$jour, kpi[, sel[i]] + ect, col=i+1, lwd=3, lty=2)
    }
    if (sprintf("%s_q10", sel[i]) %in% names(kpi)){
      q10 <- kpi[, sprintf("%s_q10", sel[i])]
      lines(kpi$jour, q10, col=i+1, lwd=1, lty=3)
    }
    if (sprintf("%s_q90", sel[i]) %in% names(kpi)){
      q90 <- kpi[, sprintf("%s_q90", sel[i])]
      lines(kpi$jour, q90, col=i+1, lwd=1, lty=3)
    }      
    lines(kpi$jour, kpi[, sel[i]], col=i+1, lwd=5)
    if (ref) abline(h=references[sel[i]], col=i+1, lwd=2, lty=4)
    
    
  }
  legend("topleft", sel, fill=1+(1:length(sel)), bty="n", cex = 0.8, y.intersp = 0.7)
}

### Trace la répartition du cumul des colonnes sélectionnées.
### - sel  : (vecteur) des noms des colonnes à afficher
repartition <- function(sel){
  barplot(sapply(sel, function(s) sum(kpi[,s])), col=1+(1:length(sel)), cex.names =.8)
  legend("topleft", sel, fill=1+(1:length(sel)), bty="n", cex = 0.8, y.intersp = 0.7)
}

### ===========================================================================
### Exemples de graphiques

#names(kpi) ## Pour connaître le nom de toutes les colonnes

if (PDF)  pdf(sprintf("%s.pdf", INSTANCE), paper="a4r", width=11.69, height=8.27)

layout(mat=matrix(1:4, nrow=2, byrow=T)) # 4 graphiques par page
par(mar=c(3.2,3.2,0.2,0.2))              # marges réduites

evolution(selection(c("ventes_prevues$", "ventes_faites$", "ventes_ratees$")), "nombre de ventes")#, ylim=c(0,20))
#evolution(selection(c("prod"), exclure="cout"), "niveaux de production des usines", ref=TRUE)
evolution(selection(c("stock$"), exclure="cout"), "niveaux des stocks", ref=TRUE)
#evolution(selection("cout_stock$"), "coûts des stocks")
evolution(selection("qte$"), "quantités transportées")
repartition(selection("cout", exclure=c("ect", "q10", "q90")))
if (PDF) dev.off()
