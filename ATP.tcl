# Musgaard lab, Ottawa Feb 2020
# Maria Musgaard

#4NTW 
#4NTW 
mol new /home/uottawa.o.univ/rdean064/MD_runs/6JIY_RYR2_open_ATP/6JIY_RYR2_open_ATP/charmm-gui-7660589534/gromacs/step5_charmm2gmx.pdb
mol addfile /home/uottawa.o.univ/rdean064/MD_runs/6JIY_RYR2_open_ATP/6JIY_RYR2_open_ATP/charmm-gui-7660589534/gromacs/Open_ATP_skip8_whole_nojump_center_res.xtc step 10 waitfor all
set open [molinfo top]



#get number of frames
set totframes [molinfo $open get numframes]

# res is the resolution of the representations
set res         30

#Aligning 


set outdir /home/uottawa.o.univ/rdean064/Figures
set outname RyR2_ATP_3

set TACHYONBIN /usr/local/lib/vmd/tachyon_LINUXAMD64
source /home/uottawa.o.univ/rdean064/Figures/vmd_colourdefs.tcl

#display depthcue on
display ambientocclusion on
#ambient, useful values 0.7 to 1.0
display aoambient 0.9
#direct, useful values 0.0 to 0.4
display aodirect 0.4
display rendermode GLSL
display projection Orthographic
color Display Background white
axes location off
display resize 900 900


#Need five colours (?) for protein chains in total for pentameric.
#Colours chosen by colorbrewer
#Need these colours in a different brightness as well for ENM
#color change rgb red 0.89412 0.10196 0.10980
color change rgb pink 1 0.55 0.50
#color change rgb blue 0.21569 0.490196 0.721569
color change rgb blue2 0.6 0.8 1
color change rgb green 0.30196 0.68627 0.290196
color change rgb green2 0.8 1 0.8 
color change rgb purple 0.596078 0.30588 0.635294 
color change rgb violet 0.85 0.60 0.90
color change rgb orange 1 0.4980 0
color change rgb orange2 1 0.8 0.35

animate goto 501
mol delrep 0 0 
mol selection resid 2344 to 2362
mol representation "NewCartoon 0.300000 $res 4.1000000"
mol material Opaque
mol color ColorID 0
mol addrep 0
mol selection resid 2711 to 2760
mol representation "NewCartoon 0.300000 $res 4.1000000"
mol material Opaque
mol color ColorID 1
mol addrep 0
mol selection protein and resid 1 to 2343 2363 to 2710 2761 to 4000
mol representation "NewCartoon 0.300000 $res 4.1000000"
mol material Transparent
mol color ColorID 6
mol addrep 0
mol selection resname ATP 
mol material Opaque
mol color Name
mol representation Licorice 0.300000 12.000000 12.000000
mol addrep 0
mol color Name
mol representation Licorice 0.300000 12.000000 12.000000
mol selection protein and resid 2348 to 2352 2755 2762 2763
mol material Opaque
mol addrep 0



source /home/uottawa.o.univ/rdean064/Figures/view_change_render.tcl 
source /home/uottawa.o.univ/rdean064/Figures//ATP_Pocket/ATP_vp.tcl
retrieve_vp 2



render Tachyon [file join $outdir ${outname}.dat] $TACHYONBIN -aasamples 12 %s -format TARGA -o %s.tga
puts "Rendering fig [file join $outdir ${outname}.tga]"





exit


