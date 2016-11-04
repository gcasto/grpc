# GRPC Node gyp file
# This currently builds the Node extension and dependencies
# This file has been automatically generated from a template file.
# Please look at the templates directory instead.
# This file can be regenerated from the template by running
# tools/buildgen/generate_projects.sh

# Copyright 2015, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Some of this file is built with the help of
# https://n8.io/converting-a-c-library-to-gyp/
{
  'target_defaults': {
    'include_dirs': [
      '.',
      'include'
    ],
    'defines': [
      'GRPC_UV'
    ],
    'conditions': [
      ['OS == "win"', {
        "include_dirs": [
          "third_party/boringssl/include",
          "third_party/zlib"
        ],
        "defines": [
          '_WIN32_WINNT=0x0600',
          'WIN32_LEAN_AND_MEAN',
          '_HAS_EXCEPTIONS=0',
          'UNICODE',
          '_UNICODE',
          'NOMINMAX',
          'OPENSSL_NO_ASM',
          'GPR_BACKWARDS_COMPATIBILITY_MODE'
        ],
        "msvs_settings": {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1, # static debug
          }
        },
        "libraries": [
          "ws2_32"
        ]
      }, { # OS != "win"
        'variables': {
          'config': '<!(echo $CONFIG)',
          # The output of "node --version" is "v[version]". We use cut to
          # remove the first character.
          'target%': '<!(node --version | cut -c2-)'
        },
          # Empirically, Node only exports ALPN symbols if its major version is >0.
          # io.js always reports versions >0 and always exports ALPN symbols.
          # Therefore, Node's major version will be truthy if and only if it
          # supports ALPN. The target is "[major].[minor].[patch]". We split by
          # periods and take the first field to get the major version.
        'defines': [
          'TSI_OPENSSL_ALPN_SUPPORT=<!(echo <(target) | cut -d. -f1)',
          'GPR_BACKWARDS_COMPATIBILITY_MODE'
        ],
        'include_dirs': [
          '<(node_root_dir)/deps/openssl/openssl/include',
          '<(node_root_dir)/deps/zlib'
        ],
        'conditions': [
          ['config=="gcov"', {
            'cflags': [
              '-ftest-coverage',
              '-fprofile-arcs',
              '-O0'
            ],
            'ldflags': [
              '-ftest-coverage',
              '-fprofile-arcs'
            ]
          }
         ],
         ["target_arch=='ia32'", {
             "include_dirs": [ "<(node_root_dir)/deps/openssl/config/piii" ]
         }],
         ["target_arch=='x64'", {
             "include_dirs": [ "<(node_root_dir)/deps/openssl/config/k8" ]
         }],
         ["target_arch=='arm'", {
             "include_dirs": [ "<(node_root_dir)/deps/openssl/config/arm" ]
         }]
        ]
      }]
    ]
  },
  'conditions': [
    ['OS == "win"', {
      'targets': [
        {
          # IMPORTANT WINDOWS BUILD INFORMATION
          # This library does not build on Windows without modifying the Node
          # development packages that node-gyp downloads in order to build.
          # Due to https://github.com/nodejs/node/issues/4932, the headers for
          # BoringSSL conflict with the OpenSSL headers included by default
          # when including the Node headers. The remedy for this is to remove
          # the OpenSSL headers, from the downloaded Node development package,
          # which is typically located in `.node-gyp` in your home directory.
          'target_name': 'WINDOWS_BUILD_WARNING',
          'actions': [
            {
              'action_name': 'WINDOWS_BUILD_WARNING',
              'inputs': [
                'package.json'
              ],
              'outputs': [
                'ignore_this_part'
              ],
              'action': ['echo', 'IMPORTANT: Due to https://github.com/nodejs/node/issues/4932, to build this library on Windows, you must first remove <(node_root_dir)/include/node/openssl/']
            }
          ]
        },
        # Only want to compile BoringSSL and zlib under Windows
      ]
    }]
  ],
  'targets': [
    {
      'cflags': [
        '-std=c99',
        '-Wall',
        '-Werror'
      ],
      'target_name': 'gpr',
      'product_prefix': 'lib',
      'type': 'static_library',
      'dependencies': [
      ],
      'sources': [
        'src/core/lib/profiling/basic_timers.c',
        'src/core/lib/profiling/stap_timers.c',
        'src/core/lib/support/alloc.c',
        'src/core/lib/support/avl.c',
        'src/core/lib/support/backoff.c',
        'src/core/lib/support/cmdline.c',
        'src/core/lib/support/cpu_iphone.c',
        'src/core/lib/support/cpu_linux.c',
        'src/core/lib/support/cpu_posix.c',
        'src/core/lib/support/cpu_windows.c',
        'src/core/lib/support/env_linux.c',
        'src/core/lib/support/env_posix.c',
        'src/core/lib/support/env_windows.c',
        'src/core/lib/support/histogram.c',
        'src/core/lib/support/host_port.c',
        'src/core/lib/support/log.c',
        'src/core/lib/support/log_android.c',
        'src/core/lib/support/log_linux.c',
        'src/core/lib/support/log_posix.c',
        'src/core/lib/support/log_windows.c',
        'src/core/lib/support/mpscq.c',
        'src/core/lib/support/murmur_hash.c',
        'src/core/lib/support/percent_encoding.c',
        'src/core/lib/support/slice.c',
        'src/core/lib/support/slice_buffer.c',
        'src/core/lib/support/stack_lockfree.c',
        'src/core/lib/support/string.c',
        'src/core/lib/support/string_posix.c',
        'src/core/lib/support/string_util_windows.c',
        'src/core/lib/support/string_windows.c',
        'src/core/lib/support/subprocess_posix.c',
        'src/core/lib/support/subprocess_windows.c',
        'src/core/lib/support/sync.c',
        'src/core/lib/support/sync_posix.c',
        'src/core/lib/support/sync_windows.c',
        'src/core/lib/support/thd.c',
        'src/core/lib/support/thd_posix.c',
        'src/core/lib/support/thd_windows.c',
        'src/core/lib/support/time.c',
        'src/core/lib/support/time_posix.c',
        'src/core/lib/support/time_precise.c',
        'src/core/lib/support/time_windows.c',
        'src/core/lib/support/tls_pthread.c',
        'src/core/lib/support/tmpfile_msys.c',
        'src/core/lib/support/tmpfile_posix.c',
        'src/core/lib/support/tmpfile_windows.c',
        'src/core/lib/support/wrap_memcpy.c',
      ],
      "conditions": [
        ['OS == "mac"', {
          'xcode_settings': {
            'MACOSX_DEPLOYMENT_TARGET': '10.9'
          }
        }]
      ]
    },
    {
      'cflags': [
        '-std=c99',
        '-Wall',
        '-Werror'
      ],
      'target_name': 'grpc',
      'product_prefix': 'lib',
      'type': 'static_library',
      'dependencies': [
        'gpr',
      ],
      'sources': [
        'src/core/lib/surface/init.c',
        'src/core/lib/channel/channel_args.c',
        'src/core/lib/channel/channel_stack.c',
        'src/core/lib/channel/channel_stack_builder.c',
        'src/core/lib/channel/compress_filter.c',
        'src/core/lib/channel/connected_channel.c',
        'src/core/lib/channel/deadline_filter.c',
        'src/core/lib/channel/handshaker.c',
        'src/core/lib/channel/http_client_filter.c',
        'src/core/lib/channel/http_server_filter.c',
        'src/core/lib/channel/message_size_filter.c',
        'src/core/lib/compression/compression.c',
        'src/core/lib/compression/message_compress.c',
        'src/core/lib/debug/trace.c',
        'src/core/lib/http/format_request.c',
        'src/core/lib/http/httpcli.c',
        'src/core/lib/http/parser.c',
        'src/core/lib/iomgr/closure.c',
        'src/core/lib/iomgr/combiner.c',
        'src/core/lib/iomgr/endpoint.c',
        'src/core/lib/iomgr/endpoint_pair_posix.c',
        'src/core/lib/iomgr/endpoint_pair_uv.c',
        'src/core/lib/iomgr/endpoint_pair_windows.c',
        'src/core/lib/iomgr/error.c',
        'src/core/lib/iomgr/ev_epoll_linux.c',
        'src/core/lib/iomgr/ev_poll_and_epoll_posix.c',
        'src/core/lib/iomgr/ev_poll_posix.c',
        'src/core/lib/iomgr/ev_posix.c',
        'src/core/lib/iomgr/exec_ctx.c',
        'src/core/lib/iomgr/executor.c',
        'src/core/lib/iomgr/iocp_windows.c',
        'src/core/lib/iomgr/iomgr.c',
        'src/core/lib/iomgr/iomgr_posix.c',
        'src/core/lib/iomgr/iomgr_uv.c',
        'src/core/lib/iomgr/iomgr_windows.c',
        'src/core/lib/iomgr/load_file.c',
        'src/core/lib/iomgr/network_status_tracker.c',
        'src/core/lib/iomgr/polling_entity.c',
        'src/core/lib/iomgr/pollset_set_uv.c',
        'src/core/lib/iomgr/pollset_set_windows.c',
        'src/core/lib/iomgr/pollset_uv.c',
        'src/core/lib/iomgr/pollset_windows.c',
        'src/core/lib/iomgr/resolve_address_posix.c',
        'src/core/lib/iomgr/resolve_address_uv.c',
        'src/core/lib/iomgr/resolve_address_windows.c',
        'src/core/lib/iomgr/resource_quota.c',
        'src/core/lib/iomgr/sockaddr_utils.c',
        'src/core/lib/iomgr/socket_utils_common_posix.c',
        'src/core/lib/iomgr/socket_utils_linux.c',
        'src/core/lib/iomgr/socket_utils_posix.c',
        'src/core/lib/iomgr/socket_utils_uv.c',
        'src/core/lib/iomgr/socket_utils_windows.c',
        'src/core/lib/iomgr/socket_windows.c',
        'src/core/lib/iomgr/tcp_client_posix.c',
        'src/core/lib/iomgr/tcp_client_uv.c',
        'src/core/lib/iomgr/tcp_client_windows.c',
        'src/core/lib/iomgr/tcp_posix.c',
        'src/core/lib/iomgr/tcp_server_posix.c',
        'src/core/lib/iomgr/tcp_server_uv.c',
        'src/core/lib/iomgr/tcp_server_windows.c',
        'src/core/lib/iomgr/tcp_uv.c',
        'src/core/lib/iomgr/tcp_windows.c',
        'src/core/lib/iomgr/time_averaged_stats.c',
        'src/core/lib/iomgr/timer_generic.c',
        'src/core/lib/iomgr/timer_heap.c',
        'src/core/lib/iomgr/timer_uv.c',
        'src/core/lib/iomgr/udp_server.c',
        'src/core/lib/iomgr/unix_sockets_posix.c',
        'src/core/lib/iomgr/unix_sockets_posix_noop.c',
        'src/core/lib/iomgr/wakeup_fd_cv.c',
        'src/core/lib/iomgr/wakeup_fd_eventfd.c',
        'src/core/lib/iomgr/wakeup_fd_nospecial.c',
        'src/core/lib/iomgr/wakeup_fd_pipe.c',
        'src/core/lib/iomgr/wakeup_fd_posix.c',
        'src/core/lib/iomgr/workqueue_uv.c',
        'src/core/lib/iomgr/workqueue_windows.c',
        'src/core/lib/json/json.c',
        'src/core/lib/json/json_reader.c',
        'src/core/lib/json/json_string.c',
        'src/core/lib/json/json_writer.c',
        'src/core/lib/surface/alarm.c',
        'src/core/lib/surface/api_trace.c',
        'src/core/lib/surface/byte_buffer.c',
        'src/core/lib/surface/byte_buffer_reader.c',
        'src/core/lib/surface/call.c',
        'src/core/lib/surface/call_details.c',
        'src/core/lib/surface/call_log_batch.c',
        'src/core/lib/surface/channel.c',
        'src/core/lib/surface/channel_init.c',
        'src/core/lib/surface/channel_ping.c',
        'src/core/lib/surface/channel_stack_type.c',
        'src/core/lib/surface/completion_queue.c',
        'src/core/lib/surface/event_string.c',
        'src/core/lib/surface/lame_client.c',
        'src/core/lib/surface/metadata_array.c',
        'src/core/lib/surface/server.c',
        'src/core/lib/surface/validate_metadata.c',
        'src/core/lib/surface/version.c',
        'src/core/lib/transport/byte_stream.c',
        'src/core/lib/transport/connectivity_state.c',
        'src/core/lib/transport/mdstr_hash_table.c',
        'src/core/lib/transport/metadata.c',
        'src/core/lib/transport/metadata_batch.c',
        'src/core/lib/transport/method_config.c',
        'src/core/lib/transport/pid_controller.c',
        'src/core/lib/transport/static_metadata.c',
        'src/core/lib/transport/timeout_encoding.c',
        'src/core/lib/transport/transport.c',
        'src/core/lib/transport/transport_op_string.c',
        'src/core/ext/transport/chttp2/server/secure/server_secure_chttp2.c',
        'src/core/ext/transport/chttp2/transport/bin_decoder.c',
        'src/core/ext/transport/chttp2/transport/bin_encoder.c',
        'src/core/ext/transport/chttp2/transport/chttp2_plugin.c',
        'src/core/ext/transport/chttp2/transport/chttp2_transport.c',
        'src/core/ext/transport/chttp2/transport/frame_data.c',
        'src/core/ext/transport/chttp2/transport/frame_goaway.c',
        'src/core/ext/transport/chttp2/transport/frame_ping.c',
        'src/core/ext/transport/chttp2/transport/frame_rst_stream.c',
        'src/core/ext/transport/chttp2/transport/frame_settings.c',
        'src/core/ext/transport/chttp2/transport/frame_window_update.c',
        'src/core/ext/transport/chttp2/transport/hpack_encoder.c',
        'src/core/ext/transport/chttp2/transport/hpack_parser.c',
        'src/core/ext/transport/chttp2/transport/hpack_table.c',
        'src/core/ext/transport/chttp2/transport/huffsyms.c',
        'src/core/ext/transport/chttp2/transport/incoming_metadata.c',
        'src/core/ext/transport/chttp2/transport/parsing.c',
        'src/core/ext/transport/chttp2/transport/status_conversion.c',
        'src/core/ext/transport/chttp2/transport/stream_lists.c',
        'src/core/ext/transport/chttp2/transport/stream_map.c',
        'src/core/ext/transport/chttp2/transport/varint.c',
        'src/core/ext/transport/chttp2/transport/writing.c',
        'src/core/ext/transport/chttp2/alpn/alpn.c',
        'src/core/lib/http/httpcli_security_connector.c',
        'src/core/lib/security/context/security_context.c',
        'src/core/lib/security/credentials/composite/composite_credentials.c',
        'src/core/lib/security/credentials/credentials.c',
        'src/core/lib/security/credentials/credentials_metadata.c',
        'src/core/lib/security/credentials/fake/fake_credentials.c',
        'src/core/lib/security/credentials/google_default/credentials_generic.c',
        'src/core/lib/security/credentials/google_default/google_default_credentials.c',
        'src/core/lib/security/credentials/iam/iam_credentials.c',
        'src/core/lib/security/credentials/jwt/json_token.c',
        'src/core/lib/security/credentials/jwt/jwt_credentials.c',
        'src/core/lib/security/credentials/jwt/jwt_verifier.c',
        'src/core/lib/security/credentials/oauth2/oauth2_credentials.c',
        'src/core/lib/security/credentials/plugin/plugin_credentials.c',
        'src/core/lib/security/credentials/ssl/ssl_credentials.c',
        'src/core/lib/security/transport/client_auth_filter.c',
        'src/core/lib/security/transport/handshake.c',
        'src/core/lib/security/transport/secure_endpoint.c',
        'src/core/lib/security/transport/security_connector.c',
        'src/core/lib/security/transport/server_auth_filter.c',
        'src/core/lib/security/transport/tsi_error.c',
        'src/core/lib/security/util/b64.c',
        'src/core/lib/security/util/json_util.c',
        'src/core/lib/surface/init_secure.c',
        'src/core/lib/tsi/fake_transport_security.c',
        'src/core/lib/tsi/ssl_transport_security.c',
        'src/core/lib/tsi/transport_security.c',
        'src/core/ext/transport/chttp2/client/secure/secure_channel_create.c',
        'src/core/ext/client_channel/channel_connectivity.c',
        'src/core/ext/client_channel/client_channel.c',
        'src/core/ext/client_channel/client_channel_factory.c',
        'src/core/ext/client_channel/client_channel_plugin.c',
        'src/core/ext/client_channel/connector.c',
        'src/core/ext/client_channel/default_initial_connect_string.c',
        'src/core/ext/client_channel/http_connect_handshaker.c',
        'src/core/ext/client_channel/initial_connect_string.c',
        'src/core/ext/client_channel/lb_policy.c',
        'src/core/ext/client_channel/lb_policy_factory.c',
        'src/core/ext/client_channel/lb_policy_registry.c',
        'src/core/ext/client_channel/parse_address.c',
        'src/core/ext/client_channel/resolver.c',
        'src/core/ext/client_channel/resolver_factory.c',
        'src/core/ext/client_channel/resolver_registry.c',
        'src/core/ext/client_channel/subchannel.c',
        'src/core/ext/client_channel/subchannel_index.c',
        'src/core/ext/client_channel/uri_parser.c',
        'src/core/ext/transport/chttp2/server/insecure/server_chttp2.c',
        'src/core/ext/transport/chttp2/server/insecure/server_chttp2_posix.c',
        'src/core/ext/transport/chttp2/client/insecure/channel_create.c',
        'src/core/ext/transport/chttp2/client/insecure/channel_create_posix.c',
        'src/core/ext/lb_policy/grpclb/grpclb.c',
        'src/core/ext/lb_policy/grpclb/load_balancer_api.c',
        'src/core/ext/lb_policy/grpclb/proto/grpc/lb/v1/load_balancer.pb.c',
        'third_party/nanopb/pb_common.c',
        'third_party/nanopb/pb_decode.c',
        'third_party/nanopb/pb_encode.c',
        'src/core/ext/lb_policy/pick_first/pick_first.c',
        'src/core/ext/lb_policy/round_robin/round_robin.c',
        'src/core/ext/resolver/dns/native/dns_resolver.c',
        'src/core/ext/resolver/sockaddr/sockaddr_resolver.c',
        'src/core/ext/load_reporting/load_reporting.c',
        'src/core/ext/load_reporting/load_reporting_filter.c',
        'src/core/ext/census/base_resources.c',
        'src/core/ext/census/context.c',
        'src/core/ext/census/gen/census.pb.c',
        'src/core/ext/census/gen/trace_context.pb.c',
        'src/core/ext/census/grpc_context.c',
        'src/core/ext/census/grpc_filter.c',
        'src/core/ext/census/grpc_plugin.c',
        'src/core/ext/census/initialize.c',
        'src/core/ext/census/mlog.c',
        'src/core/ext/census/operation.c',
        'src/core/ext/census/placeholders.c',
        'src/core/ext/census/resource.c',
        'src/core/ext/census/trace_context.c',
        'src/core/ext/census/tracing.c',
        'src/core/plugin_registry/grpc_plugin_registry.c',
      ],
      "conditions": [
        ['OS == "mac"', {
          'xcode_settings': {
            'MACOSX_DEPLOYMENT_TARGET': '10.9'
          }
        }]
      ]
    },
    {
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'cflags': [
        '-std=c++11',
        '-Wall',
        '-pthread',
        '-g',
        '-zdefs',
        '-Werror',
        '-Wno-error=deprecated-declarations'
      ],
      'ldflags': [
        '-g'
      ],
      "conditions": [
        ['OS=="mac"', {
          'xcode_settings': {
            'MACOSX_DEPLOYMENT_TARGET': '10.9',
            'OTHER_CFLAGS': [
              '-stdlib=libc++',
              '-std=c++11'
            ]
          }
        }],
        ['OS=="win"', {
          'dependencies': [
            "boringssl",
            "z",
          ]
        }],
        ['OS=="linux"', {
          'ldflags': [
            '-Wl,-wrap,memcpy'
          ]
        }]
      ],
      "target_name": "grpc_node",
      "sources": [
        "src/node/ext/byte_buffer.cc",
        "src/node/ext/call.cc",
        "src/node/ext/call_credentials.cc",
        "src/node/ext/channel.cc",
        "src/node/ext/channel_credentials.cc",
        "src/node/ext/completion_queue.cc",
        "src/node/ext/completion_queue_async_worker.cc",
        "src/node/ext/node_grpc.cc",
        "src/node/ext/server.cc",
        "src/node/ext/server_credentials.cc",
        "src/node/ext/timeval.cc",
      ],
      "dependencies": [
        "grpc",
        "gpr",
      ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node"],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
