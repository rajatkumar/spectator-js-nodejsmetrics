{
  'targets': [
    {
      'target_name': 'spectator_internals',
      'dependencies': [],
      'sources': ["internals/functions.cc"],
      'include_dirs' : [
        "<!(node -e \"require('nan')\")"
      ],
      'conditions': [
        [ 'OS=="mac"', {
          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS' : ['-stdlib=libc++', '-v', '-std=c++14', '-Wall', '-Wextra', '-Wno-unused-parameter', '-g', '-O2' ],
            'OTHER_LDFLAGS': ['-stdlib=libc++'],
            'MACOSX_DEPLOYMENT_TARGET': '10.12',
            'GCC_ENABLE_CPP_EXCEPTIONS': 'NO'
          }
        }],
        ['OS=="linux"', {
          'cflags': ['-std=c++14', '-Wall', '-Wextra', '-Wno-unused-parameter', '-g', '-O2' ]
        }]
      ]
    }
  ]
}

