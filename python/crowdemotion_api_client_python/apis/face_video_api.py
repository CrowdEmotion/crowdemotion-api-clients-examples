# coding: utf-8

"""
    CloudEmotion API v1

    CrowdEmotion API

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class FaceVideoApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def facevideo_facevideo_id_delete(self, facevideo_id, **kwargs):
        """
        Delete a FaceVideo
        <p>Use this operation to delete a FaceVideo.</p> <p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.facevideo_facevideo_id_delete(facevideo_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int facevideo_id: ID of FaceVideo to be deleted. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.facevideo_facevideo_id_delete_with_http_info(facevideo_id, **kwargs)
        else:
            (data) = self.facevideo_facevideo_id_delete_with_http_info(facevideo_id, **kwargs)
            return data

    def facevideo_facevideo_id_delete_with_http_info(self, facevideo_id, **kwargs):
        """
        Delete a FaceVideo
        <p>Use this operation to delete a FaceVideo.</p> <p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.facevideo_facevideo_id_delete_with_http_info(facevideo_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int facevideo_id: ID of FaceVideo to be deleted. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['facevideo_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method facevideo_facevideo_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'facevideo_id' is set
        if ('facevideo_id' not in params) or (params['facevideo_id'] is None):
            raise ValueError("Missing the required parameter `facevideo_id` when calling `facevideo_facevideo_id_delete`")

        resource_path = '/facevideo/{facevideo_id}'.replace('{format}', 'json')
        path_params = {}
        if 'facevideo_id' in params:
            path_params['facevideo_id'] = params['facevideo_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def facevideo_get(self, **kwargs):
        """
        Find a FaceVideo
        <p>Use this operation to access information about the FaceVideo analysis.</p> <p><i>Any one of the two parameters must be specified.</i></p> <p>To discover if the video has been analyzed, check the meaning of status field in the following table:</p> <table>   <tr><td>Value</td> <td>Description</td></tr>   <tr><td>0</td> <td>Not started</td></tr>   <tr><td>1</td> <td>Processing started</td></tr>   <tr><td>2</td> <td>Processing completed</td></tr>   <tr><td>-1</td> <td>Error</td></tr> </table> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.facevideo_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int facevideo_id: FaceVideo ID. NOTE: Only this parameter is considered if both are specified.
        :param int response_id: Response ID corresponding to the FaceVideo.
        :return: FaceVideo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.facevideo_get_with_http_info(**kwargs)
        else:
            (data) = self.facevideo_get_with_http_info(**kwargs)
            return data

    def facevideo_get_with_http_info(self, **kwargs):
        """
        Find a FaceVideo
        <p>Use this operation to access information about the FaceVideo analysis.</p> <p><i>Any one of the two parameters must be specified.</i></p> <p>To discover if the video has been analyzed, check the meaning of status field in the following table:</p> <table>   <tr><td>Value</td> <td>Description</td></tr>   <tr><td>0</td> <td>Not started</td></tr>   <tr><td>1</td> <td>Processing started</td></tr>   <tr><td>2</td> <td>Processing completed</td></tr>   <tr><td>-1</td> <td>Error</td></tr> </table> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.facevideo_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int facevideo_id: FaceVideo ID. NOTE: Only this parameter is considered if both are specified.
        :param int response_id: Response ID corresponding to the FaceVideo.
        :return: FaceVideo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['facevideo_id', 'response_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method facevideo_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/facevideo'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'facevideo_id' in params:
            query_params['facevideo_id'] = params['facevideo_id']
        if 'response_id' in params:
            query_params['response_id'] = params['response_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='FaceVideo',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def facevideo_post(self, **kwargs):
        """
        Analyse FaceVideo
        <p>Starts the analysis of a single FaceVideo (in the supported formats) through either:</p> <ol>   <li>a video URL pointing to a resource accessible through the Internet without authentication</li>   <li>the binary contents of the video in the request's body, encoded as <code>multipart/form-data</code> content type</li> </ol> <p>The third option is a <code>PUT</code> call to <code>/v1/facevideo/{filename}</code> (<code>filename</code> required string e.g. <code>facevideo1.mp4</code>) which supports all the URL parameters as above with a body encoding <code>application/octet-stream</code> and the file contents as plain binary: this call makes uploads more efficient but it does not respect HTTP/RESTful standards so it may be not supported in future.</p> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.facevideo_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file filename: FaceVideo to be analysed.
        :param bool sandbox: Generates random data for testing, at no cost. Default: false.
        :param int response_id: Associates this Facevideo to a previously generated Response.
        :param int research_id: Associates this Facevideo to a previously generated Research.
        :param int media_id: Associates this Facevideo to a previously generated Media.
        :param int respondent_id: Associates this Facevideo to a previously generated Respondent.
        :param bool process_video: Actually processes the video. Default: true.
        :return: FaceVideo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.facevideo_post_with_http_info(**kwargs)
        else:
            (data) = self.facevideo_post_with_http_info(**kwargs)
            return data

    def facevideo_post_with_http_info(self, **kwargs):
        """
        Analyse FaceVideo
        <p>Starts the analysis of a single FaceVideo (in the supported formats) through either:</p> <ol>   <li>a video URL pointing to a resource accessible through the Internet without authentication</li>   <li>the binary contents of the video in the request's body, encoded as <code>multipart/form-data</code> content type</li> </ol> <p>The third option is a <code>PUT</code> call to <code>/v1/facevideo/{filename}</code> (<code>filename</code> required string e.g. <code>facevideo1.mp4</code>) which supports all the URL parameters as above with a body encoding <code>application/octet-stream</code> and the file contents as plain binary: this call makes uploads more efficient but it does not respect HTTP/RESTful standards so it may be not supported in future.</p> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.facevideo_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file filename: FaceVideo to be analysed.
        :param bool sandbox: Generates random data for testing, at no cost. Default: false.
        :param int response_id: Associates this Facevideo to a previously generated Response.
        :param int research_id: Associates this Facevideo to a previously generated Research.
        :param int media_id: Associates this Facevideo to a previously generated Media.
        :param int respondent_id: Associates this Facevideo to a previously generated Respondent.
        :param bool process_video: Actually processes the video. Default: true.
        :return: FaceVideo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filename', 'sandbox', 'response_id', 'research_id', 'media_id', 'respondent_id', 'process_video']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method facevideo_post" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/facevideo'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sandbox' in params:
            query_params['sandbox'] = params['sandbox']
        if 'response_id' in params:
            query_params['response_id'] = params['response_id']
        if 'research_id' in params:
            query_params['research_id'] = params['research_id']
        if 'media_id' in params:
            query_params['media_id'] = params['media_id']
        if 'respondent_id' in params:
            query_params['respondent_id'] = params['respondent_id']
        if 'process_video' in params:
            query_params['processVideo'] = params['process_video']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'filename' in params:
            local_var_files['filename'] = params['filename']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='FaceVideo',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def facevideo_put(self, **kwargs):
        """
        Analyse FaceVideo
        <p>Starts the analysis of a single FaceVideo (in the supported formats) through either:</p> <ol>   <li>a video URL pointing to a resource accessible through the Internet without authentication</li>   <li>the binary contents of the video in the request's body, encoded as <code>multipart/form-data</code> content type</li> </ol> <p>The third option is a <code>PUT</code> call to <code>/v1/facevideo/{filename}</code> (<code>filename</code> required string e.g. <code>facevideo1.mp4</code>) which supports all the URL parameters as above with a body encoding <code>application/octet-stream</code> and the file contents as plain binary: this call makes uploads more efficient but it does not respect HTTP/RESTful standards so it may be not supported in future.</p> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.facevideo_put(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool sandbox: Generates random data for testing, at no cost. Default: false.
        :param int response_id: Associates this Facevideo to a previously generated Response.
        :param int research_id: Associates this Facevideo to a previously generated Research.
        :param int media_id: Associates this Facevideo to a previously generated Media.
        :param int respondent_id: Associates this Facevideo to a previously generated Respondent.
        :param bool process_video: Actually processes the video. Default: true.
        :param FaceVideoUpload body: Request body
        :return: FaceVideo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.facevideo_put_with_http_info(**kwargs)
        else:
            (data) = self.facevideo_put_with_http_info(**kwargs)
            return data

    def facevideo_put_with_http_info(self, **kwargs):
        """
        Analyse FaceVideo
        <p>Starts the analysis of a single FaceVideo (in the supported formats) through either:</p> <ol>   <li>a video URL pointing to a resource accessible through the Internet without authentication</li>   <li>the binary contents of the video in the request's body, encoded as <code>multipart/form-data</code> content type</li> </ol> <p>The third option is a <code>PUT</code> call to <code>/v1/facevideo/{filename}</code> (<code>filename</code> required string e.g. <code>facevideo1.mp4</code>) which supports all the URL parameters as above with a body encoding <code>application/octet-stream</code> and the file contents as plain binary: this call makes uploads more efficient but it does not respect HTTP/RESTful standards so it may be not supported in future.</p> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.facevideo_put_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool sandbox: Generates random data for testing, at no cost. Default: false.
        :param int response_id: Associates this Facevideo to a previously generated Response.
        :param int research_id: Associates this Facevideo to a previously generated Research.
        :param int media_id: Associates this Facevideo to a previously generated Media.
        :param int respondent_id: Associates this Facevideo to a previously generated Respondent.
        :param bool process_video: Actually processes the video. Default: true.
        :param FaceVideoUpload body: Request body
        :return: FaceVideo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sandbox', 'response_id', 'research_id', 'media_id', 'respondent_id', 'process_video', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method facevideo_put" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/facevideo'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sandbox' in params:
            query_params['sandbox'] = params['sandbox']
        if 'response_id' in params:
            query_params['response_id'] = params['response_id']
        if 'research_id' in params:
            query_params['research_id'] = params['research_id']
        if 'media_id' in params:
            query_params['media_id'] = params['media_id']
        if 'respondent_id' in params:
            query_params['respondent_id'] = params['respondent_id']
        if 'process_video' in params:
            query_params['processVideo'] = params['process_video']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='FaceVideo',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))