### input1:
area.xyz or area.grd
### input2:
Number of points (nx, ny)
### input3:
Data file, containing lon,lat,z,a,e,isys,ib
* 注：
isys是针对求解dodson方程需要的参数，选择下面的一个system类型

1. (isys.eq.1) then
!here are Ea and D0/a2 values for AFT from ketcham. 1999
!taken from reiners 2004
      energy=147.d3!/(4.184*1.e3)
      geom=1.d0
      diff=2.05e6*3600.*24.*365.25e6 

2. (isys.eq.2) then
!here are Ea and D0/a2 values for ZFT from reiners2004
!taken from reiners 2004
      energy=208.d3!/(4.184*1.e3)
      geom=1.d0
      diff=4.0e8*3600.*24.*365.25e6
3. (isys.eq.3) then
!here are Ea and D0/a2 values for AHe from Farley et al. 2000
!taken from reiners 2004
      energy=138.d3!/(4.184*1.e3)
      geom=1.d0
      diff=7.64e7*3600.*24.*365.25e6
4. (isys.eq.4) then
!here are Ea and D0/a2 values for ZHe from reiners2004
!taken from reiners 2004
      energy=169.d3!/(4.184*1.e3)
      geom=1.d0
      diff=7.03d5*3600.d0*24.d0*365.25d6
      !endif
      
      !the following are for argon argon, might be a bit much for most, 51,52,53 in glide
5. (isys.eq.5) then
!here are Ea and D0/a2 values for hbl from harrison81
!taken from reiners 2004
      energy=268.d3!/(4.184*1.e3)
      geom=1.d0
      diff=1320*3600.*24.*365.25e6
6. (isys.eq.6) then
!here are Ea and D0/a2 values for mus from hames&bowring1994,robbins72
!taken from reiners 2004
      energy=180.d3!/(4.184*1.e3)
      geom=1.d0
      diff=3.91*3600.*24.*365.25e6
7. (isys.eq.7) then
!here are Ea and D0/a2 values for bio from grove&harrison1996
!taken from reiners 2004
      energy=197.d3!/(4.184*1.e3)
      geom=1.d0
      diff=733.*3600.*24.*365.25e6
      endif
ib是是否为block代码中默认全是即ib=1

### input4：
A priori estimate of the mean exhumation rate
### input5：
Time step length, in Myrs(默认2)
### input6：
End time，in Myrs（默认80）
### input7：
求解微分方程边界条件和相关系数
Thermal thickness (km), T_surface(C) at 0,T_base(C),diffusivity(km2/Myr),heat production(C/Myr)
默认（50. 10. 1120. 20. 0.0001）


