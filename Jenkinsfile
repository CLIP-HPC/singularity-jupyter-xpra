// build singularity container

buildSingularityImage([
    imageName: 'jupyter-xpra-demo',
    recipeFile: 'Singularity.xpra.def',
    signKeyCredentials: null,
    pushRegistry: 'singularity.vbc.ac.at',
    pushRegistryNamespace: 'clip',
    pushRegistryCredentials: 'svc-singularity-token',
    pushBranches: ['develop', 'master'],
])

