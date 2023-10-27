# load required library 
# last revised oct 24, 2023 by Luis ZA
library(picante)

# load the community table (presence absence table made from make_table.py, where rows are samples and headers are sequence header names)
comm <- read.csv(file.choose(), header = TRUE, row.names = 1)

# load the tree file associated with the community table
phy <- read.tree(file.choose())
# check class of phy
class(phy)
# plot the tree
plot(phy)
# check the first 5 tip names of the tree
phy$tip.label[1:5]
# print tbe number of tips in the tree
Ntip(phy)

# check for mismatches/missing species
combined <- match.phylo.comm(phy, comm)
# the resulting object is a list with $phy and $comm elements.  replace our
# original data with the sorted/matched data
phy.new <- combined$phy
comm.new <- combined$comm

# run the PD function, and check the head of the output
comm.pd <- pd(comm.new, phy.new, include.root = "FALSE")
head(comm.pd)
# check class of comm.pd, should be a data frame
class(comm.pd)
# write the data frame to a csv
write.csv(comm.pd,'out.csv')
specnumber(comm.new)
specnumber(comm)



# convert phylogeney to a distance matrix
phy.dist <- cophenetic(phy.new)
# calculate ses.mpd
comm.sesmpd <- ses.mpd(comm.new, phy.dist, null.model = "richness", abundance.weighted = FALSE, 
                       runs = 999)
head(comm.sesmpd)


comm.sesmntd <- ses.mntd(comm.new, phy.dist, null.model = "richness", abundance.weighted = FALSE, 
                         runs = 999)
head(comm.sesmntd)
